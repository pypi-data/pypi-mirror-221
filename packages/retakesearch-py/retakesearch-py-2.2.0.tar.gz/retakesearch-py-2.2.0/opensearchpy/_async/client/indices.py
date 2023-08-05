# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.
#
#  Licensed to Elasticsearch B.V. under one or more contributor
#  license agreements. See the NOTICE file distributed with
#  this work for additional information regarding copyright
#  ownership. Elasticsearch B.V. licenses this file to you under
#  the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.


from .utils import SKIP_IN_PATH, NamespacedClient, _make_path, query_params


class IndicesClient(NamespacedClient):
    @query_params()
    async def analyze(self, body=None, index=None, params=None, headers=None):
        """
        Performs the analysis process on a text and return the tokens breakdown of the
        text.


        :arg body: Define analyzer/tokenizer parameters and the text on
            which the analysis should be performed
        :arg index: The name of the index to scope the operation
        """
        return await self.transport.perform_request(
            "POST",
            _make_path(index, "_analyze"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params("allow_no_indices", "expand_wildcards", "ignore_unavailable")
    async def refresh(self, index=None, params=None, headers=None):
        """
        Performs the refresh operation in one or more indices.


        :arg index: A comma-separated list of index names; use `_all` or
            empty string to perform the operation on all indices
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both.  Valid choices: open,
            closed, hidden, none, all  Default: open
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed)
        """
        return await self.transport.perform_request(
            "POST", _make_path(index, "_refresh"), params=params, headers=headers
        )

    @query_params(
        "allow_no_indices",
        "expand_wildcards",
        "force",
        "ignore_unavailable",
        "wait_if_ongoing",
    )
    async def flush(self, index=None, params=None, headers=None):
        """
        Performs the flush operation on one or more indices.


        :arg index: A comma-separated list of index names; use `_all` or
            empty string for all indices
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both.  Valid choices: open,
            closed, hidden, none, all  Default: open
        :arg force: Whether a flush should be forced even if it is not
            necessarily needed ie. if no changes will be committed to the index.
            This is useful if transaction log IDs should be incremented even if no
            uncommitted changes are present. (This setting can be considered as
            internal)
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed)
        :arg wait_if_ongoing: If set to true the flush operation will
            block until the flush can be executed if another flush operation is
            already executing. The default is true. If set to false the flush will
            be skipped iff if another flush operation is already running.
        """
        return await self.transport.perform_request(
            "POST", _make_path(index, "_flush"), params=params, headers=headers
        )

    @query_params(
        "master_timeout", "cluster_manager_timeout", "timeout", "wait_for_active_shards"
    )
    async def create(self, index, body=None, params=None, headers=None):
        """
        Creates an index with optional settings and mappings.


        :arg index: The name of the index
        :arg body: The configuration for the index (`settings` and
            `mappings`)
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Specify timeout for connection to master
        :arg cluster_manager_timeout: Specify timeout for connection to cluster_manager
        :arg timeout: Explicit operation timeout
        :arg wait_for_active_shards: Set the number of active shards to
            wait for before the operation returns.
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'index'.")

        return await self.transport.perform_request(
            "PUT", _make_path(index), params=params, headers=headers, body=body
        )

    @query_params(
        "master_timeout", "cluster_manager_timeout", "timeout", "wait_for_active_shards"
    )
    async def clone(self, index, target, body=None, params=None, headers=None):
        """
        Clones an index


        :arg index: The name of the source index to clone
        :arg target: The name of the target index to clone into
        :arg body: The configuration for the target index (`settings`
            and `aliases`)
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Specify timeout for connection to master
        :arg cluster_manager_timeout: Specify timeout for connection to cluster_manager
        :arg timeout: Explicit operation timeout
        :arg wait_for_active_shards: Set the number of active shards to
            wait for on the cloned index before the operation returns.
        """
        for param in (index, target):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "PUT",
            _make_path(index, "_clone", target),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params(
        "allow_no_indices",
        "expand_wildcards",
        "flat_settings",
        "ignore_unavailable",
        "include_defaults",
        "local",
        "master_timeout",
        "cluster_manager_timeout",
    )
    async def get(self, index, params=None, headers=None):
        """
        Returns information about one or more indices.


        :arg index: A comma-separated list of index names
        :arg allow_no_indices: Ignore if a wildcard expression resolves
            to no concrete indices (default: false)
        :arg expand_wildcards: Whether wildcard expressions should get
            expanded to open or closed indices (default: open)  Valid choices: open,
            closed, hidden, none, all  Default: open
        :arg flat_settings: Return settings in flat format (default:
            false)
        :arg ignore_unavailable: Ignore unavailable indexes (default:
            false)
        :arg include_defaults: Whether to return all default setting for
            each of the indices.
        :arg local: Return local information, do not retrieve the state
            from cluster_manager node (default: false)
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Specify timeout for connection to master
        :arg cluster_manager_timeout: Specify timeout for connection to cluster_manager
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'index'.")

        return await self.transport.perform_request(
            "GET", _make_path(index), params=params, headers=headers
        )

    @query_params(
        "allow_no_indices",
        "expand_wildcards",
        "ignore_unavailable",
        "master_timeout",
        "cluster_manager_timeout",
        "timeout",
        "wait_for_active_shards",
    )
    async def open(self, index, params=None, headers=None):
        """
        Opens an index.


        :arg index: A comma separated list of indices to open
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both.  Valid choices: open,
            closed, hidden, none, all  Default: closed
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed)
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Specify timeout for connection to master
        :arg cluster_manager_timeout: Specify timeout for connection to cluster_manager
        :arg timeout: Explicit operation timeout
        :arg wait_for_active_shards: Sets the number of active shards to
            wait for before the operation returns.
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'index'.")

        return await self.transport.perform_request(
            "POST", _make_path(index, "_open"), params=params, headers=headers
        )

    @query_params(
        "allow_no_indices",
        "expand_wildcards",
        "ignore_unavailable",
        "master_timeout",
        "cluster_manager_timeout",
        "timeout",
        "wait_for_active_shards",
    )
    async def close(self, index, params=None, headers=None):
        """
        Closes an index.


        :arg index: A comma separated list of indices to close
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both.  Valid choices: open,
            closed, hidden, none, all  Default: open
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed)
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Specify timeout for connection to master
        :arg cluster_manager_timeout: Specify timeout for connection to cluster_manager
        :arg timeout: Explicit operation timeout
        :arg wait_for_active_shards: Sets the number of active shards to
            wait for before the operation returns. Set to `index-setting` to wait
            according to the index setting `index.write.wait_for_active_shards`, or
            `all` to wait for all shards, or an integer. Defaults to `0`.
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'index'.")

        return await self.transport.perform_request(
            "POST", _make_path(index, "_close"), params=params, headers=headers
        )

    @query_params(
        "allow_no_indices",
        "expand_wildcards",
        "ignore_unavailable",
        "master_timeout",
        "cluster_manager_timeout",
        "timeout",
    )
    async def delete(self, index, params=None, headers=None):
        """
        Deletes an index.


        :arg index: A comma-separated list of indices to delete; use
            `_all` or `*` string to delete all indices
        :arg allow_no_indices: Ignore if a wildcard expression resolves
            to no concrete indices (default: false)
        :arg expand_wildcards: Whether wildcard expressions should get
            expanded to open or closed indices (default: open)  Valid choices: open,
            closed, hidden, none, all  Default: open
        :arg ignore_unavailable: Ignore unavailable indexes (default:
            false)
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Specify timeout for connection to master
        :arg cluster_manager_timeout: Specify timeout for connection to cluster_manager
        :arg timeout: Explicit operation timeout
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'index'.")

        return await self.transport.perform_request(
            "DELETE", _make_path(index), params=params, headers=headers
        )

    @query_params(
        "allow_no_indices",
        "expand_wildcards",
        "flat_settings",
        "ignore_unavailable",
        "include_defaults",
        "local",
    )
    async def exists(self, index, params=None, headers=None):
        """
        Returns information about whether a particular index exists.


        :arg index: A comma-separated list of index names
        :arg allow_no_indices: Ignore if a wildcard expression resolves
            to no concrete indices (default: false)
        :arg expand_wildcards: Whether wildcard expressions should get
            expanded to open or closed indices (default: open)  Valid choices: open,
            closed, hidden, none, all  Default: open
        :arg flat_settings: Return settings in flat format (default:
            false)
        :arg ignore_unavailable: Ignore unavailable indexes (default:
            false)
        :arg include_defaults: Whether to return all default setting for
            each of the indices.
        :arg local: Return local information, do not retrieve the state
            from cluster_manager node (default: false)
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'index'.")

        return await self.transport.perform_request(
            "HEAD", _make_path(index), params=params, headers=headers
        )

    @query_params(
        "allow_no_indices",
        "expand_wildcards",
        "ignore_unavailable",
        "master_timeout",
        "cluster_manager_timeout",
        "timeout",
        "write_index_only",
    )
    async def put_mapping(self, body, index=None, params=None, headers=None):
        """
        Updates the index mappings.


        :arg body: The mapping definition
        :arg index: A comma-separated list of index names the mapping
            should be added to (supports wildcards); use `_all` or omit to add the
            mapping on all indices.
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both.  Valid choices: open,
            closed, hidden, none, all  Default: open
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed)
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Specify timeout for connection to master
        :arg cluster_manager_timeout: Specify timeout for connection to cluster_manager
        :arg timeout: Explicit operation timeout
        :arg write_index_only: When true, applies mappings only to the
            write index of an alias or data stream
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return await self.transport.perform_request(
            "PUT",
            _make_path(index, "_mapping"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params(
        "allow_no_indices",
        "expand_wildcards",
        "ignore_unavailable",
        "local",
        "master_timeout",
        "cluster_manager_timeout",
    )
    async def get_mapping(self, index=None, params=None, headers=None):
        """
        Returns mappings for one or more indices.


        :arg index: A comma-separated list of index names
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both.  Valid choices: open,
            closed, hidden, none, all  Default: open
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed)
        :arg local: Return local information, do not retrieve the state
            from cluster_manager node (default: false)
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Specify timeout for connection to master
        :arg cluster_manager_timeout: Specify timeout for connection to cluster_manager
        """
        return await self.transport.perform_request(
            "GET",
            _make_path(index, "_mapping"),
            params=params,
            headers=headers,
        )

    @query_params(
        "allow_no_indices",
        "expand_wildcards",
        "ignore_unavailable",
        "include_defaults",
        "local",
    )
    async def get_field_mapping(self, fields, index=None, params=None, headers=None):
        """
        Returns mapping for one or more fields.


        :arg fields: A comma-separated list of fields
        :arg index: A comma-separated list of index names
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both.  Valid choices: open,
            closed, hidden, none, all  Default: open
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed)
        :arg include_defaults: Whether the default mapping values should
            be returned as well
        :arg local: Return local information, do not retrieve the state
            from cluster_manager node (default: false)
        """
        if fields in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'fields'.")

        return await self.transport.perform_request(
            "GET",
            _make_path(index, "_mapping", "field", fields),
            params=params,
            headers=headers,
        )

    @query_params("master_timeout", "cluster_manager_timeout", "timeout")
    async def put_alias(self, index, name, body=None, params=None, headers=None):
        """
        Creates or updates an alias.


        :arg index: A comma-separated list of index names the alias
            should point to (supports wildcards); use `_all` to perform the
            operation on all indices.
        :arg name: The name of the alias to be created or updated
        :arg body: The settings for the alias, such as `routing` or
            `filter`
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Specify timeout for connection to master
        :arg cluster_manager_timeout: Specify timeout for connection to cluster_manager
        :arg timeout: Explicit timestamp for the document
        """
        for param in (index, name):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "PUT",
            _make_path(index, "_alias", name),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params("allow_no_indices", "expand_wildcards", "ignore_unavailable", "local")
    async def exists_alias(self, name, index=None, params=None, headers=None):
        """
        Returns information about whether a particular alias exists.


        :arg name: A comma-separated list of alias names to return
        :arg index: A comma-separated list of index names to filter
            aliases
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both.  Valid choices: open,
            closed, hidden, none, all  Default: all
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed)
        :arg local: Return local information, do not retrieve the state
            from cluster_manager node (default: false)
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'name'.")

        return await self.transport.perform_request(
            "HEAD", _make_path(index, "_alias", name), params=params, headers=headers
        )

    @query_params("allow_no_indices", "expand_wildcards", "ignore_unavailable", "local")
    async def get_alias(self, index=None, name=None, params=None, headers=None):
        """
        Returns an alias.


        :arg index: A comma-separated list of index names to filter
            aliases
        :arg name: A comma-separated list of alias names to return
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both.  Valid choices: open,
            closed, hidden, none, all  Default: all
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed)
        :arg local: Return local information, do not retrieve the state
            from cluster_manager node (default: false)
        """
        return await self.transport.perform_request(
            "GET", _make_path(index, "_alias", name), params=params, headers=headers
        )

    @query_params("master_timeout", "cluster_manager_timeout", "timeout")
    async def update_aliases(self, body, params=None, headers=None):
        """
        Updates index aliases.


        :arg body: The definition of `actions` to perform
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Specify timeout for connection to master
        :arg cluster_manager_timeout: Specify timeout for connection to cluster_manager
        :arg timeout: Request timeout
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return await self.transport.perform_request(
            "POST", "/_aliases", params=params, headers=headers, body=body
        )

    @query_params("master_timeout", "cluster_manager_timeout", "timeout")
    async def delete_alias(self, index, name, params=None, headers=None):
        """
        Deletes an alias.


        :arg index: A comma-separated list of index names (supports
            wildcards); use `_all` for all indices
        :arg name: A comma-separated list of aliases to delete (supports
            wildcards); use `_all` to delete all aliases for the specified indices.
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Specify timeout for connection to master
        :arg cluster_manager_timeout: Specify timeout for connection to cluster_manager
        :arg timeout: Explicit timestamp for the document
        """
        for param in (index, name):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "DELETE", _make_path(index, "_alias", name), params=params, headers=headers
        )

    @query_params("create", "master_timeout", "cluster_manager_timeout", "order")
    async def put_template(self, name, body, params=None, headers=None):
        """
        Creates or updates an index template.


        :arg name: The name of the template
        :arg body: The template definition
        :arg create: Whether the index template should only be added if
            new or can also replace an existing one
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Specify timeout for connection to master
        :arg cluster_manager_timeout: Specify timeout for connection to cluster_manager
        :arg order: The order for this template when merging multiple
            matching ones (higher numbers are merged later, overriding the lower
            numbers)
        """
        for param in (name, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "PUT",
            _make_path("_template", name),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params("flat_settings", "local", "master_timeout", "cluster_manager_timeout")
    async def exists_template(self, name, params=None, headers=None):
        """
        Returns information about whether a particular index template exists.


        :arg name: The comma separated names of the index templates
        :arg flat_settings: Return settings in flat format (default:
            false)
        :arg local: Return local information, do not retrieve the state
            from cluster_manager node (default: false)
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Explicit operation timeout for connection
            to master node
        :arg cluster_manager_timeout: Explicit operation timeout for connection
            to cluster_manager node
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'name'.")

        return await self.transport.perform_request(
            "HEAD", _make_path("_template", name), params=params, headers=headers
        )

    @query_params("flat_settings", "local", "master_timeout", "cluster_manager_timeout")
    async def get_template(self, name=None, params=None, headers=None):
        """
        Returns an index template.


        :arg name: The comma separated names of the index templates
        :arg flat_settings: Return settings in flat format (default:
            false)
        :arg local: Return local information, do not retrieve the state
            from cluster_manager node (default: false)
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Explicit operation timeout for connection
            to master node
        :arg cluster_manager_timeout: Explicit operation timeout for connection
            to cluster_manager node
        """
        return await self.transport.perform_request(
            "GET", _make_path("_template", name), params=params, headers=headers
        )

    @query_params("master_timeout", "cluster_manager_timeout", "timeout")
    async def delete_template(self, name, params=None, headers=None):
        """
        Deletes an index template.


        :arg name: The name of the template
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Specify timeout for connection to master
        :arg cluster_manager_timeout: Specify timeout for connection to cluster_manager
        :arg timeout: Explicit operation timeout
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'name'.")

        return await self.transport.perform_request(
            "DELETE", _make_path("_template", name), params=params, headers=headers
        )

    @query_params(
        "allow_no_indices",
        "expand_wildcards",
        "flat_settings",
        "ignore_unavailable",
        "include_defaults",
        "local",
        "master_timeout",
        "cluster_manager_timeout",
    )
    async def get_settings(self, index=None, name=None, params=None, headers=None):
        """
        Returns settings for one or more indices.


        :arg index: A comma-separated list of index names; use `_all` or
            empty string to perform the operation on all indices
        :arg name: The name of the settings that should be included
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both.  Valid choices: open,
            closed, hidden, none, all  Default: all
        :arg flat_settings: Return settings in flat format (default:
            false)
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed)
        :arg include_defaults: Whether to return all default setting for
            each of the indices.
        :arg local: Return local information, do not retrieve the state
            from cluster_manager node (default: false)
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Specify timeout for connection to master
        :arg cluster_manager_timeout: Specify timeout for connection to cluster_manager
        """
        return await self.transport.perform_request(
            "GET", _make_path(index, "_settings", name), params=params, headers=headers
        )

    @query_params(
        "allow_no_indices",
        "expand_wildcards",
        "flat_settings",
        "ignore_unavailable",
        "master_timeout",
        "cluster_manager_timeout",
        "preserve_existing",
        "timeout",
    )
    async def put_settings(self, body, index=None, params=None, headers=None):
        """
        Updates the index settings.


        :arg body: The index settings to be updated
        :arg index: A comma-separated list of index names; use `_all` or
            empty string to perform the operation on all indices
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both.  Valid choices: open,
            closed, hidden, none, all  Default: open
        :arg flat_settings: Return settings in flat format (default:
            false)
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed)
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Specify timeout for connection to master
        :arg cluster_manager_timeout: Specify timeout for connection to cluster_manager
        :arg preserve_existing: Whether to update existing settings. If
            set to `true` existing settings on an index remain unchanged, the
            default is `false`
        :arg timeout: Explicit operation timeout
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return await self.transport.perform_request(
            "PUT",
            _make_path(index, "_settings"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params(
        "completion_fields",
        "expand_wildcards",
        "fielddata_fields",
        "fields",
        "forbid_closed_indices",
        "groups",
        "include_segment_file_sizes",
        "include_unloaded_segments",
        "level",
        "types",
    )
    async def stats(self, index=None, metric=None, params=None, headers=None):
        """
        Provides statistics on operations happening in an index.


        :arg index: A comma-separated list of index names; use `_all` or
            empty string to perform the operation on all indices
        :arg metric: Limit the information returned the specific
            metrics.  Valid choices: _all, completion, docs, fielddata, query_cache,
            flush, get, indexing, merge, request_cache, refresh, search, segments,
            store, warmer, suggest
        :arg completion_fields: A comma-separated list of fields for
            `fielddata` and `suggest` index metric (supports wildcards)
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both.  Valid choices: open,
            closed, hidden, none, all  Default: open
        :arg fielddata_fields: A comma-separated list of fields for
            `fielddata` index metric (supports wildcards)
        :arg fields: A comma-separated list of fields for `fielddata`
            and `completion` index metric (supports wildcards)
        :arg forbid_closed_indices: If set to false stats will also
            collected from closed indices if explicitly specified or if
            expand_wildcards expands to closed indices  Default: True
        :arg groups: A comma-separated list of search groups for
            `search` index metric
        :arg include_segment_file_sizes: Whether to report the
            aggregated disk usage of each one of the Lucene index files (only
            applies if segment stats are requested)
        :arg include_unloaded_segments: If set to true segment stats
            will include stats for segments that are not currently loaded into
            memory
        :arg level: Return stats aggregated at cluster, index or shard
            level  Valid choices: cluster, indices, shards  Default: indices
        :arg types: A comma-separated list of document types for the
            `indexing` index metric
        """
        return await self.transport.perform_request(
            "GET", _make_path(index, "_stats", metric), params=params, headers=headers
        )

    @query_params(
        "allow_no_indices", "expand_wildcards", "ignore_unavailable", "verbose"
    )
    async def segments(self, index=None, params=None, headers=None):
        """
        Provides low-level information about segments in a Lucene index.


        :arg index: A comma-separated list of index names; use `_all` or
            empty string to perform the operation on all indices
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both.  Valid choices: open,
            closed, hidden, none, all  Default: open
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed)
        :arg verbose: Includes detailed memory usage by Lucene.
        """
        return await self.transport.perform_request(
            "GET", _make_path(index, "_segments"), params=params, headers=headers
        )

    @query_params(
        "all_shards",
        "allow_no_indices",
        "analyze_wildcard",
        "analyzer",
        "default_operator",
        "df",
        "expand_wildcards",
        "explain",
        "ignore_unavailable",
        "lenient",
        "q",
        "rewrite",
    )
    async def validate_query(self, body=None, index=None, params=None, headers=None):
        """
        Allows a user to validate a potentially expensive query without executing it.


        :arg body: The query definition specified with the Query DSL
        :arg index: A comma-separated list of index names to restrict
            the operation; use `_all` or empty string to perform the operation on
            all indices
        :arg all_shards: Execute validation on all shards instead of one
            random shard per index
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg analyze_wildcard: Specify whether wildcard and prefix
            queries should be analyzed (default: false)
        :arg analyzer: The analyzer to use for the query string
        :arg default_operator: The default operator for query string
            query (AND or OR)  Valid choices: AND, OR  Default: OR
        :arg df: The field to use as default where no field prefix is
            given in the query string
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both.  Valid choices: open,
            closed, hidden, none, all  Default: open
        :arg explain: Return detailed information about the error
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed)
        :arg lenient: Specify whether format-based query failures (such
            as providing text to a numeric field) should be ignored
        :arg q: Query in the Lucene query string syntax
        :arg rewrite: Provide a more detailed explanation showing the
            actual Lucene query that will be executed.
        """
        return await self.transport.perform_request(
            "POST",
            _make_path(index, "_validate", "query"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params(
        "allow_no_indices",
        "expand_wildcards",
        "fielddata",
        "fields",
        "ignore_unavailable",
        "query",
        "request",
    )
    async def clear_cache(self, index=None, params=None, headers=None):
        """
        Clears all or specific caches for one or more indices.


        :arg index: A comma-separated list of index name to limit the
            operation
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both.  Valid choices: open,
            closed, hidden, none, all  Default: open
        :arg fielddata: Clear field data
        :arg fields: A comma-separated list of fields to clear when
            using the `fielddata` parameter (default: all)
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed)
        :arg query: Clear query caches
        :arg request: Clear request cache
        """
        return await self.transport.perform_request(
            "POST", _make_path(index, "_cache", "clear"), params=params, headers=headers
        )

    @query_params("active_only", "detailed")
    async def recovery(self, index=None, params=None, headers=None):
        """
        Returns information about ongoing index shard recoveries.


        :arg index: A comma-separated list of index names; use `_all` or
            empty string to perform the operation on all indices
        :arg active_only: Display only those recoveries that are
            currently on-going
        :arg detailed: Whether to display detailed information about
            shard recovery
        """
        return await self.transport.perform_request(
            "GET", _make_path(index, "_recovery"), params=params, headers=headers
        )

    @query_params(
        "allow_no_indices",
        "expand_wildcards",
        "ignore_unavailable",
        "only_ancient_segments",
        "wait_for_completion",
    )
    async def upgrade(self, index=None, params=None, headers=None):
        """
        DEPRECATED Upgrades to the current version of Lucene.


        :arg index: A comma-separated list of index names; use `_all` or
            empty string to perform the operation on all indices
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both.  Valid choices: open,
            closed, hidden, none, all  Default: open
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed)
        :arg only_ancient_segments: If true, only ancient (an older
            Lucene major release) segments will be upgraded
        :arg wait_for_completion: Specify whether the request should
            block until the all segments are upgraded (default: false)
        """
        return await self.transport.perform_request(
            "POST", _make_path(index, "_upgrade"), params=params, headers=headers
        )

    @query_params("allow_no_indices", "expand_wildcards", "ignore_unavailable")
    async def get_upgrade(self, index=None, params=None, headers=None):
        """
        DEPRECATED Returns a progress status of current upgrade.


        :arg index: A comma-separated list of index names; use `_all` or
            empty string to perform the operation on all indices
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both.  Valid choices: open,
            closed, hidden, none, all  Default: open
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed)
        """
        return await self.transport.perform_request(
            "GET", _make_path(index, "_upgrade"), params=params, headers=headers
        )

    @query_params(
        "allow_no_indices", "expand_wildcards", "ignore_unavailable", "status"
    )
    async def shard_stores(self, index=None, params=None, headers=None):
        """
        Provides store information for shard copies of indices.


        :arg index: A comma-separated list of index names; use `_all` or
            empty string to perform the operation on all indices
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both.  Valid choices: open,
            closed, hidden, none, all  Default: open
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed)
        :arg status: A comma-separated list of statuses used to filter
            on shards to get store information for  Valid choices: green, yellow,
            red, all
        """
        return await self.transport.perform_request(
            "GET", _make_path(index, "_shard_stores"), params=params, headers=headers
        )

    @query_params(
        "allow_no_indices",
        "expand_wildcards",
        "flush",
        "ignore_unavailable",
        "max_num_segments",
        "only_expunge_deletes",
    )
    async def forcemerge(self, index=None, params=None, headers=None):
        """
        Performs the force merge operation on one or more indices.


        :arg index: A comma-separated list of index names; use `_all` or
            empty string to perform the operation on all indices
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both.  Valid choices: open,
            closed, hidden, none, all  Default: open
        :arg flush: Specify whether the index should be flushed after
            performing the operation (default: true)
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed)
        :arg max_num_segments: The number of segments the index should
            be merged into (default: dynamic)
        :arg only_expunge_deletes: Specify whether the operation should
            only expunge deleted documents
        """
        return await self.transport.perform_request(
            "POST", _make_path(index, "_forcemerge"), params=params, headers=headers
        )

    @query_params(
        "copy_settings",
        "master_timeout",
        "cluster_manager_timeout",
        "timeout",
        "wait_for_active_shards",
    )
    async def shrink(self, index, target, body=None, params=None, headers=None):
        """
        Allow to shrink an existing index into a new index with fewer primary shards.


        :arg index: The name of the source index to shrink
        :arg target: The name of the target index to shrink into
        :arg body: The configuration for the target index (`settings`
            and `aliases`)
        :arg copy_settings: whether or not to copy settings from the
            source index (defaults to false)
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Specify timeout for connection to master
        :arg cluster_manager_timeout: Specify timeout for connection to cluster_manager
        :arg timeout: Explicit operation timeout
        :arg wait_for_active_shards: Set the number of active shards to
            wait for on the shrunken index before the operation returns.
        """
        for param in (index, target):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "PUT",
            _make_path(index, "_shrink", target),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params(
        "copy_settings",
        "master_timeout",
        "cluster_manager_timeout",
        "timeout",
        "wait_for_active_shards",
    )
    async def split(self, index, target, body=None, params=None, headers=None):
        """
        Allows you to split an existing index into a new index with more primary
        shards.


        :arg index: The name of the source index to split
        :arg target: The name of the target index to split into
        :arg body: The configuration for the target index (`settings`
            and `aliases`)
        :arg copy_settings: whether or not to copy settings from the
            source index (defaults to false)
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Specify timeout for connection to master
        :arg cluster_manager_timeout: Specify timeout for connection to cluster_manager
        :arg timeout: Explicit operation timeout
        :arg wait_for_active_shards: Set the number of active shards to
            wait for on the shrunken index before the operation returns.
        """
        for param in (index, target):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "PUT",
            _make_path(index, "_split", target),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params(
        "dry_run",
        "master_timeout",
        "cluster_manager_timeout",
        "timeout",
        "wait_for_active_shards",
    )
    async def rollover(
        self, alias, body=None, new_index=None, params=None, headers=None
    ):
        """
        Updates an alias to point to a new index when the existing index is considered
        to be too large or too old.


        :arg alias: The name of the alias to rollover
        :arg body: The conditions that needs to be met for executing
            rollover
        :arg new_index: The name of the rollover index
        :arg dry_run: If set to true the rollover action will only be
            validated but not actually performed even if a condition matches. The
            default is false
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Specify timeout for connection to master
        :arg cluster_manager_timeout: Specify timeout for connection to cluster_manager
        :arg timeout: Explicit operation timeout
        :arg wait_for_active_shards: Set the number of active shards to
            wait for on the newly created rollover index before the operation
            returns.
        """
        if alias in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'alias'.")

        return await self.transport.perform_request(
            "POST",
            _make_path(alias, "_rollover", new_index),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params(
        "allow_no_indices",
        "expand_wildcards",
        "ignore_unavailable",
        "master_timeout",
        "cluster_manager_timeout",
        "timeout",
        "wait_for_active_shards",
    )
    async def freeze(self, index, params=None, headers=None):
        """
        Freezes an index. A frozen index has almost no overhead on the cluster (except
        for maintaining its metadata in memory) and is read-only.


        :arg index: The name of the index to freeze
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both.  Valid choices: open,
            closed, hidden, none, all  Default: closed
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed)
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Specify timeout for connection to master
        :arg cluster_manager_timeout: Specify timeout for connection to cluster_manager
        :arg timeout: Explicit operation timeout
        :arg wait_for_active_shards: Sets the number of active shards to
            wait for before the operation returns.
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'index'.")

        return await self.transport.perform_request(
            "POST", _make_path(index, "_freeze"), params=params, headers=headers
        )

    @query_params(
        "allow_no_indices",
        "expand_wildcards",
        "ignore_unavailable",
        "master_timeout",
        "cluster_manager_timeout",
        "timeout",
        "wait_for_active_shards",
    )
    async def unfreeze(self, index, params=None, headers=None):
        """
        Unfreezes an index. When a frozen index is unfrozen, the index goes through the
        normal recovery process and becomes writeable again.


        :arg index: The name of the index to unfreeze
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both.  Valid choices: open,
            closed, hidden, none, all  Default: closed
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed)
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Specify timeout for connection to master
        :arg cluster_manager_timeout: Specify timeout for connection to cluster_manager
        :arg timeout: Explicit operation timeout
        :arg wait_for_active_shards: Sets the number of active shards to
            wait for before the operation returns.
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'index'.")

        return await self.transport.perform_request(
            "POST", _make_path(index, "_unfreeze"), params=params, headers=headers
        )

    @query_params("allow_no_indices", "expand_wildcards", "ignore_unavailable")
    async def reload_search_analyzers(self, index, params=None, headers=None):
        """
        Reloads an index's search analyzers and their resources.


        :arg index: A comma-separated list of index names to reload
            analyzers for
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both.  Valid choices: open,
            closed, hidden, none, all  Default: open
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed)
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'index'.")

        return await self.transport.perform_request(
            "GET",
            _make_path(index, "_reload_search_analyzers"),
            params=params,
            headers=headers,
        )

    @query_params()
    async def create_data_stream(self, name, params=None, headers=None):
        """
        Creates a data stream


        :arg name: The name of the data stream
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'name'.")

        return await self.transport.perform_request(
            "PUT", _make_path("_data_stream", name), params=params, headers=headers
        )

    @query_params("expand_wildcards")
    async def delete_data_stream(self, name, params=None, headers=None):
        """
        Deletes a data stream.


        :arg name: A comma-separated list of data streams to delete; use
            `*` to delete all data streams
        :arg expand_wildcards: Whether wildcard expressions should get
            expanded to open or closed indices (default: open)  Valid choices: open,
            closed, hidden, none, all  Default: open
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'name'.")

        return await self.transport.perform_request(
            "DELETE", _make_path("_data_stream", name), params=params, headers=headers
        )

    @query_params("master_timeout", "cluster_manager_timeout", "timeout")
    async def delete_index_template(self, name, params=None, headers=None):
        """
        Deletes an index template.


        :arg name: The name of the template
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Specify timeout for connection to master
        :arg cluster_manager_timeout: Specify timeout for connection to cluster_manager
        :arg timeout: Explicit operation timeout
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'name'.")

        return await self.transport.perform_request(
            "DELETE",
            _make_path("_index_template", name),
            params=params,
            headers=headers,
        )

    @query_params("flat_settings", "local", "master_timeout", "cluster_manager_timeout")
    async def exists_index_template(self, name, params=None, headers=None):
        """
        Returns information about whether a particular index template exists.


        :arg name: The name of the template
        :arg flat_settings: Return settings in flat format (default:
            false)
        :arg local: Return local information, do not retrieve the state
            from cluster_manager node (default: false)
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Explicit operation timeout for connection
            to master node
        :arg cluster_manager_timeout: Explicit operation timeout for connection
            to cluster_manager node
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'name'.")

        return await self.transport.perform_request(
            "HEAD", _make_path("_index_template", name), params=params, headers=headers
        )

    @query_params("flat_settings", "local", "master_timeout", "cluster_manager_timeout")
    async def get_index_template(self, name=None, params=None, headers=None):
        """
        Returns an index template.


        :arg name: The comma separated names of the index templates
        :arg flat_settings: Return settings in flat format (default:
            false)
        :arg local: Return local information, do not retrieve the state
            from cluster_manager node (default: false)
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Explicit operation timeout for connection
            to master node
        :arg cluster_manager_timeout: Explicit operation timeout for connection
            to cluster_manager node
        """
        return await self.transport.perform_request(
            "GET", _make_path("_index_template", name), params=params, headers=headers
        )

    @query_params("cause", "create", "master_timeout", "cluster_manager_timeout")
    async def put_index_template(self, name, body, params=None, headers=None):
        """
        Creates or updates an index template.


        :arg name: The name of the template
        :arg body: The template definition
        :arg cause: User defined reason for creating/updating the index
            template
        :arg create: Whether the index template should only be added if
            new or can also replace an existing one
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Specify timeout for connection to master
        :arg cluster_manager_timeout: Specify timeout for connection to cluster_manager
        """
        for param in (name, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "PUT",
            _make_path("_index_template", name),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params("cause", "create", "master_timeout", "cluster_manager_timeout")
    async def simulate_index_template(self, name, body=None, params=None, headers=None):
        """
        Simulate matching the given index name against the index templates in the
        system


        :arg name: The name of the index (it must be a concrete index
            name)
        :arg body: New index template definition, which will be included
            in the simulation, as if it already exists in the system
        :arg cause: User defined reason for dry-run creating the new
            template for simulation purposes
        :arg create: Whether the index template we optionally defined in
            the body should only be dry-run added if new or can also replace an
            existing one
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Specify timeout for connection to master
        :arg cluster_manager_timeout: Specify timeout for connection to cluster_manager
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'name'.")

        return await self.transport.perform_request(
            "POST",
            _make_path("_index_template", "_simulate_index", name),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params("expand_wildcards")
    async def get_data_stream(self, name=None, params=None, headers=None):
        """
        Returns data streams.


        :arg name: A comma-separated list of data streams to get; use
            `*` to get all data streams
        :arg expand_wildcards: Whether wildcard expressions should get
            expanded to open or closed indices (default: open)  Valid choices: open,
            closed, hidden, none, all  Default: open
        """
        return await self.transport.perform_request(
            "GET", _make_path("_data_stream", name), params=params, headers=headers
        )

    @query_params("cause", "create", "master_timeout", "cluster_manager_timeout")
    async def simulate_template(self, body=None, name=None, params=None, headers=None):
        """
        Simulate resolving the given template name or body


        :arg body: New index template definition to be simulated, if no
            index template name is specified
        :arg name: The name of the index template
        :arg cause: User defined reason for dry-run creating the new
            template for simulation purposes
        :arg create: Whether the index template we optionally defined in
            the body should only be dry-run added if new or can also replace an
            existing one
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Specify timeout for connection to master
        :arg cluster_manager_timeout: Specify timeout for connection to cluster_manager
        """
        return await self.transport.perform_request(
            "POST",
            _make_path("_index_template", "_simulate", name),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params("expand_wildcards")
    async def resolve_index(self, name, params=None, headers=None):
        """
        Returns information about any matching indices, aliases, and data streams


        .. warning::

            This API is **experimental** so may include breaking changes
            or be removed in a future version

        :arg name: A comma-separated list of names or wildcard
            expressions
        :arg expand_wildcards: Whether wildcard expressions should get
            expanded to open or closed indices (default: open)  Valid choices: open,
            closed, hidden, none, all  Default: open
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'name'.")

        return await self.transport.perform_request(
            "GET", _make_path("_resolve", "index", name), params=params, headers=headers
        )

    @query_params(
        "allow_no_indices",
        "expand_wildcards",
        "ignore_unavailable",
        "master_timeout",
        "cluster_manager_timeout",
        "timeout",
    )
    async def add_block(self, index, block, params=None, headers=None):
        """
        Adds a block to an index.


        :arg index: A comma separated list of indices to add a block to
        :arg block: The block to add (one of read, write, read_only or
            metadata)
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both.  Valid choices: open,
            closed, hidden, none, all  Default: open
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed)
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Specify timeout for connection to master
        :arg cluster_manager_timeout: Specify timeout for connection to cluster_manager
        :arg timeout: Explicit operation timeout
        """
        for param in (index, block):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "PUT", _make_path(index, "_block", block), params=params, headers=headers
        )

    @query_params()
    async def data_streams_stats(self, name=None, params=None, headers=None):
        """
        Provides statistics on operations happening in a data stream.


        :arg name: A comma-separated list of data stream names; use
            `_all` or empty string to perform the operation on all data streams
        """
        return await self.transport.perform_request(
            "GET",
            _make_path("_data_stream", name, "_stats"),
            params=params,
            headers=headers,
        )

    @query_params()
    async def promote_data_stream(self, name, params=None, headers=None):
        """
        Promotes a data stream from a replicated data stream managed by CCR to a
        regular data stream


        :arg name: The name of the data stream
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'name'.")

        return await self.transport.perform_request(
            "POST",
            _make_path("_data_stream", "_promote", name),
            params=params,
            headers=headers,
        )

    @query_params()
    async def migrate_to_data_stream(self, name, params=None, headers=None):
        """
        Migrates an alias to a data stream


        :arg name: The name of the alias to migrate
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'name'.")

        return await self.transport.perform_request(
            "POST",
            _make_path("_data_stream", "_migrate", name),
            params=params,
            headers=headers,
        )

    @query_params(
        "allow_no_indices",
        "expand_wildcards",
        "flush",
        "ignore_unavailable",
        "run_expensive_tasks",
    )
    async def disk_usage(self, index, params=None, headers=None):
        """
        Analyzes the disk usage of each field of an index or data stream


        .. warning::

            This API is **experimental** so may include breaking changes
            or be removed in a future version

        :arg index: Comma-separated list of indices or data streams to
            analyze the disk usage
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both.  Valid choices: open,
            closed, hidden, none, all  Default: open
        :arg flush: Whether flush or not before analyzing the index disk
            usage. Defaults to true
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed)
        :arg run_expensive_tasks: Must be set to [true] in order for the
            task to be performed. Defaults to false.
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'index'.")

        return await self.transport.perform_request(
            "POST", _make_path(index, "_disk_usage"), params=params, headers=headers
        )

    @query_params(
        "allow_no_indices", "expand_wildcards", "fields", "ignore_unavailable"
    )
    async def field_usage_stats(self, index, params=None, headers=None):
        """
        Returns the field usage stats for each field of an index


        .. warning::

            This API is **experimental** so may include breaking changes
            or be removed in a future version

        :arg index: A comma-separated list of index names; use `_all` or
            empty string to perform the operation on all indices
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both.  Valid choices: open,
            closed, hidden, none, all  Default: open
        :arg fields: A comma-separated list of fields to include in the
            stats if only a subset of fields should be returned (supports wildcards)
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed)
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'index'.")

        return await self.transport.perform_request(
            "GET",
            _make_path(index, "_field_usage_stats"),
            params=params,
            headers=headers,
        )
