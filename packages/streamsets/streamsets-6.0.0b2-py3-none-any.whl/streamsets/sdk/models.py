# Copyright 2019 StreamSets Inc.

"""Models to be used by multiple StreamSets components."""

import inflection
import json

json_to_python_style = lambda x: inflection.underscore(x)
python_to_json_style = lambda x: inflection.camelize(x, uppercase_first_letter=False)


class Configuration:
    """Abstraction for stage configurations.

    This class enables easy access to and modification of data stored as a list of dictionaries. As
    an example, SDC's pipeline configuration is stored in the form

    .. code-block:: none

        [ {
          "name" : "executionMode",
          "value" : "STANDALONE"
        }, {
          "name" : "deliveryGuarantee",
          "value" : "AT_LEAST_ONCE"
        }, ... ]

    By implementing simple ``__getitem__`` and ``__setitem__`` methods, this class allows items in
    this list to be accessed using

    .. code-block:: python

        configuration['executionMode'] = 'CLUSTER_BATCH'

    Instead of the more verbose

    .. code-block:: python

        for property in configuration:
            if property['name'] == 'executionMode':
                property['value'] = 'CLUSTER_BATCH'
            break

    Args:
        configuration (:obj:`list`): List of dictionaries comprising the configuration.
        property_key (:obj:`str`, optional): The dictionary entry denoting the property key.
            Default: ``name``
        property_value (:obj:`str`, optional): The dictionary entry denoting the property value.
            Default: ``value``
        update_callable (optional): A callable to which ``self._data`` will be passed as part of ``__setitem__``.
        update_callable_kwargs (:obj:`dict`, optional): A dictionary of kwargs to pass (along with a body)
            to the callable.
        id_to_remap (:obj:`dict`, optional): A dictionary mapping configuration IDs to human-readable container keys.
                                             Example: {'custom_region':'googleCloudConfig.customRegion', ... }
    """

    # Use an uber secret class attribute to specify whether other attributes can be assigned by __setattr__.
    __frozen = False

    def __init__(self, configuration=None, property_key='name', property_value='value',
                 update_callable=None, update_callable_kwargs=None, id_to_remap=None):
        self._data = configuration
        self.property_key = property_key
        self.property_value = property_value
        self._id_to_remap = id_to_remap or {}
        self._update_callable = update_callable
        self._update_callable_kwargs = update_callable_kwargs or {}
        self._configuration_index_map = {config[self.property_key]: index for index, config in enumerate(self._data)}
        self.__frozen = True

    def __getattr__(self, key):
        if not self.__frozen:
            super().__getattr__(key)
            return

        return self.__getitem__(key)

    def __getitem__(self, key):
        if key in self._id_to_remap:
            key = self._id_to_remap[key]

        if key not in self._configuration_index_map:
            raise AttributeError(key)

        index = self._configuration_index_map[key]
        config = self._data[index]
        return self._convert_value(config)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        if not self.__frozen:
            super().__setattr__(key, value)
            return

        if key in self._id_to_remap:
            key = self._id_to_remap[key]

        if key not in self._configuration_index_map:
            raise AttributeError(key)

        index = self._configuration_index_map[key]
        config = self._data[index]

        config[self.property_value] = value
        if self._update_callable:
            kwargs = dict(body=[config])
            kwargs.update(self._update_callable_kwargs)
            self._update_callable(**kwargs)

    def __contains__(self, item):
        return item in self._id_to_remap or item in self._configuration_index_map

    def __repr__(self):
        configs = {}
        for config in self._data:
            key = config[self.property_key]
            configs[key] = self._convert_value(config)

        # If a key has a remapped key, delete the original key and add the remapped key into configs
        for remapped_key, original_key in self._id_to_remap.items():
            if original_key in configs:
                configs[remapped_key] = configs[original_key]
                del configs[original_key]

        return '{{{}}}'.format(', '.join("'{}': {}".format(k, v) for k, v in configs.items()))

    def __dir__(self):
        # Stripping out any values that have multiple words in it. Example: 'Organization account type'
        # in sch_models.Organization.configuration
        id_to_remap_cleaned = [key for key in self._id_to_remap.keys() if ' ' not in key]
        return sorted(list(dir(object)) + list(self.__dict__.keys()) + id_to_remap_cleaned)

    def items(self):
        """Gets the configuration's items.

        Returns:
            A new view of the configuration’s items ((key, value) pairs).
        """
        # To keep the behavior in line with a Python dict's, we'll generate one and then use its items method.
        configuration_dict = {config[self.property_key]: config[self.property_value] for config in self._data}
        for config_property in self._id_to_remap:
            key = self._id_to_remap[config_property]
            if key in configuration_dict:
                configuration_dict[config_property] = configuration_dict[key]
                del configuration_dict[key]
        return configuration_dict.items()

    def get(self, key, default=None):
        """Return the value of key or, if not in the configuration, the default value."""
        try:
            return self[key]
        except KeyError:
            return default

    def update(self, configs):
        """Update instance with a collection of configurations.

        Args:
            configs (:obj:`dict`): Dictionary of configurations to use.
        """
        for key, value in configs.items():
            self[key] = value

    def _convert_value(self, config):
        if config.get('type') == 'boolean':
            return json.loads(config[self.property_value])
        elif config.get('type') == 'integer':
            return int(config[self.property_value])
        else:
            return config[self.property_value]


class BaseModel:
    """Base class for StreamSets Accounts models that essentially just wrap a dictionary.

    Args:
        data (:obj:`dict`): The underlying JSON representation of the model.
        attributes_to_ignore (:obj:`list`, optional): A list of string attributes to mask from being handled
            by this class' __setattr__ method. Default: ``None``.
        attributes_to_remap (:obj:`dict`, optional): A dictionary of attributes to remap with the desired attributes
            as keys and the corresponding property name in the JSON representation as values. Default: ``None``.
        repr_metadata (:obj:`list`, optional): A list of attributes to use in the model's __repr__ string.
            Default: ``None``.
    """

    def __init__(self, data, attributes_to_ignore=None, attributes_to_remap=None, repr_metadata=None):
        # _data_internal is introduced to  help inherited classes that need to load _data when _data is accessed
        # eg. Pipeline
        super().__setattr__('_data_internal', data)
        super().__setattr__('_attributes_to_ignore', attributes_to_ignore or [])
        super().__setattr__('_attributes_to_remap', attributes_to_remap or {})
        super().__setattr__('_repr_metadata', repr_metadata or [])

    # By default these properties don't do anything by can be overrided by inherited classes to load something
    @property
    def _data_internal(self):
        return self.__dict__['_data'] if '_data' in self.__dict__ else None

    @_data_internal.setter
    def _data_internal(self, data):
        self.__dict__['_data'] = data

    @property
    def _data(self):
        return self._data_internal

    @_data.setter
    def _data(self, data):
        self._data_internal = data

    def __getattr__(self, name):
        name_ = python_to_json_style(name)
        if name in self._attributes_to_remap:
            remapped_name = self._attributes_to_remap[name]
            return self._data_internal[remapped_name]
        elif (name_ in self._data_internal and
              name not in self._attributes_to_ignore and
              name not in self._attributes_to_remap.values()):
            return self._data_internal[name_]
        raise AttributeError('Could not find attribute {}.'.format(name_))

    def __setattr__(self, name, value):
        name_ = python_to_json_style(name)
        if name in self._attributes_to_remap:
            remapped_name = self._attributes_to_remap[name]
            self._data_internal[remapped_name] = value
        elif (name_ in self._data_internal and
              name not in self._attributes_to_ignore and
              name not in self._attributes_to_remap.values()):
            self._data_internal[name_] = value
        else:
            super().__setattr__(name, value)

    def __dir__(self):
        return sorted(list(dir(object))
                      + list(self.__dict__.keys())
                      + list(json_to_python_style(key)
                             for key in self._data_internal.keys()
                             if key not in (list(self._attributes_to_remap.values())
                                            + self._attributes_to_ignore))
                      + list(self._attributes_to_remap.keys()))

    def __eq__(self, other):
        return self._data_internal == other._data_internal

    def __repr__(self):
        return '<{} ({})>'.format(self.__class__.__name__,
                                  ', '.join('{}={}'.format(key, getattr(self, key)) for key in self._repr_metadata))


class ModelCollection:
    """Base class wrapper with Abstractions.

    Args:
        streamsets_entity: An instance of underlysing StreamSets entity
            e.g. :py:class:`streamsets.sdk.next.Next` or :py:class:`streamsets.sdk.accounts.Accounts`.
    """

    def __init__(self, streamsets_entity):
        self._streamsets_entity = streamsets_entity
        self._id_attr = 'id'

    def _get_all_results_from_api(self, **kwargs):
        """Used to get multiple (all) results from api.

        Args:
            Optional arguments to be passed to filter the results.

        Returns:
            A :obj:`collections.namedtuple`: of
                results (:py:class:`streamsets.sdk.utils.SeekableList`): a SeekableList of inherited instances of
                :py:class:`streamsets.sdk.models.BaseModel` and
                kwargs (:obj:`dict`): a dict of local variables not used in this function.
        """
        pass

    def __iter__(self):
        """Enables the list enumeration or iteration."""
        for item in self._get_all_results_from_api().results:
            yield item

    def __getitem__(self, i):
        """Enables the user to fetch items by index.

        Args:
            i (:obj:`int`): Index of the item.

        Returns:
            An inherited instance of :py:class:`streamsets.sdk.models.BaseModel`.
        """
        return self._get_all_results_from_api().results[i]

    def __len__(self):
        """Provides length (count) of items.

        Returns:
            A :py:obj:`int` object.
        """
        return len(self._get_all_results_from_api().results)

    def __contains__(self, item_given):
        """Checks if given item is in the list of items by comparing the ids.

        Returns:
            A :py:obj:`boolean` object.
        """
        return self.contains(**{self._id_attr: getattr(item_given, self._id_attr)})

    def get(self, **kwargs):
        """
        Args:
            **kwargs: Optional arguments to be passed to filter the results offline.

        Returns:
            An inherited instance of :py:class:`streamsets.sdk.models.BaseModel`.
        """
        result, new_kwargs = self._get_all_results_from_api(**kwargs)
        return result.get(**new_kwargs)

    def get_all(self, **kwargs):
        """
        Args:
            **kwargs: Optional other arguments to be passed to filter the results offline.

        Returns:
            A :py:obj:`streamsets.sdk.utils.SeekableList` of inherited instances of
            :py:class:`streamsets.sdk.models.BaseModel`.
        """
        result, new_kwargs = self._get_all_results_from_api(**kwargs)
        return result.get_all(**new_kwargs)

    def __repr__(self):
        return str(self._get_all_results_from_api().results)

    def contains(self, **kwargs):
        """
        Args:
            **kwargs: Optional arguments to be passed to filter the results offline.

        Returns:
            A :py:obj:`boolean` object.
        """
        try:
            self.get(**kwargs)
        except ValueError:
            return False
        return True
