# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network vnet peering create",
)
class Create(AAZCommand):
    """Create a virtual network peering connection.

    To successfully peer two virtual networks this command must be called twice with the values for --vnet-name and --remote-vnet reversed.

    :example: Create a peering connection between two virtual networks.
        az network vnet peering create -g MyResourceGroup -n MyVnet1ToMyVnet2 --vnet-name MyVnet1 --remote-vnet MyVnet2Id --allow-vnet-access
    """

    _aaz_info = {
        "version": "2023-11-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/virtualnetworks/{}/virtualnetworkpeerings/{}", "2023-11-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.vnet_name = AAZStrArg(
            options=["--vnet-name"],
            help="The virtual network (VNet) name.",
            required=True,
        )
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="The name of the VNet peering.",
            required=True,
        )
        _args_schema.sync_remote = AAZStrArg(
            options=["--sync-remote"],
            help="Indicate the intention to sync the peering with the current address space on the remote VNet after it's updated.",
            enum={"true": "true"},
        )
        _args_schema.allow_forwarded_traffic = AAZBoolArg(
            options=["--allow-forwarded-traffic"],
            help="Whether the forwarded traffic from the VMs in the local virtual network will be allowed/disallowed in remote virtual network.",
            default=False,
        )
        _args_schema.allow_gateway_transit = AAZBoolArg(
            options=["--allow-gateway-transit"],
            help="If gateway links can be used in remote virtual networking to link to this virtual network.",
            default=False,
        )
        _args_schema.allow_vnet_access = AAZBoolArg(
            options=["--allow-vnet-access"],
            help="Whether the VMs in the local virtual network space would be able to access the VMs in remote virtual network space.",
            default=False,
        )
        _args_schema.enable_only_ipv6 = AAZBoolArg(
            options=["--enable-only-ipv6"],
            help="Whether only Ipv6 address space is peered for subnet peering.",
        )
        _args_schema.local_subnet_names = AAZListArg(
            options=["--local-subnet-names"],
            help="List of local subnet names that are subnet peered with remote virtual network.",
        )
        _args_schema.peer_complete_vnets = AAZBoolArg(
            options=["--peer-complete-vnets"],
            help="Whether complete virtual network address space is peered.",
        )
        _args_schema.remote_subnet_names = AAZListArg(
            options=["--remote-subnet-names"],
            help="List of remote subnet names from remote virtual network that are subnet peered.",
        )
        _args_schema.remote_vnet = AAZStrArg(
            options=["--remote-vnet"],
            help="Name or ID of the remote VNet.",
        )
        _args_schema.use_remote_gateways = AAZBoolArg(
            options=["--use-remote-gateways"],
            help="Allows VNet to use the remote VNet's gateway. Remote VNet gateway must have --allow-gateway-transit enabled for remote peering. Only 1 peering can have this flag enabled. Cannot be set if the VNet already has a gateway.",
            default=False,
        )

        local_subnet_names = cls._args_schema.local_subnet_names
        local_subnet_names.Element = AAZStrArg()

        remote_subnet_names = cls._args_schema.remote_subnet_names
        remote_subnet_names.Element = AAZStrArg()

        # define Arg Group "Properties"

        # define Arg Group "VirtualNetworkPeeringParameters"
        return cls._args_schema

    _args_address_space_create = None

    @classmethod
    def _build_args_address_space_create(cls, _schema):
        if cls._args_address_space_create is not None:
            _schema.address_prefixes = cls._args_address_space_create.address_prefixes
            return

        cls._args_address_space_create = AAZObjectArg()

        address_space_create = cls._args_address_space_create
        address_space_create.address_prefixes = AAZListArg(
            options=["address-prefixes"],
            help="A list of address blocks reserved for this virtual network in CIDR notation.",
        )

        address_prefixes = cls._args_address_space_create.address_prefixes
        address_prefixes.Element = AAZStrArg()

        _schema.address_prefixes = cls._args_address_space_create.address_prefixes

    def _execute_operations(self):
        self.pre_operations()
        yield self.VirtualNetworkPeeringsCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class VirtualNetworkPeeringsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}/virtualNetworkPeerings/{virtualNetworkPeeringName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "virtualNetworkName", self.ctx.args.vnet_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "virtualNetworkPeeringName", self.ctx.args.name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "syncRemoteAddressSpace", self.ctx.args.sync_remote,
                ),
                **self.serialize_query_param(
                    "api-version", "2023-11-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("name", AAZStrType, ".name")
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("allowForwardedTraffic", AAZBoolType, ".allow_forwarded_traffic")
                properties.set_prop("allowGatewayTransit", AAZBoolType, ".allow_gateway_transit")
                properties.set_prop("allowVirtualNetworkAccess", AAZBoolType, ".allow_vnet_access")
                properties.set_prop("enableOnlyIPv6Peering", AAZBoolType, ".enable_only_ipv6")
                properties.set_prop("localSubnetNames", AAZListType, ".local_subnet_names")
                properties.set_prop("peerCompleteVnets", AAZBoolType, ".peer_complete_vnets")
                properties.set_prop("remoteSubnetNames", AAZListType, ".remote_subnet_names")
                properties.set_prop("remoteVirtualNetwork", AAZObjectType)
                properties.set_prop("useRemoteGateways", AAZBoolType, ".use_remote_gateways")

            local_subnet_names = _builder.get(".properties.localSubnetNames")
            if local_subnet_names is not None:
                local_subnet_names.set_elements(AAZStrType, ".")

            remote_subnet_names = _builder.get(".properties.remoteSubnetNames")
            if remote_subnet_names is not None:
                remote_subnet_names.set_elements(AAZStrType, ".")

            remote_virtual_network = _builder.get(".properties.remoteVirtualNetwork")
            if remote_virtual_network is not None:
                remote_virtual_network.set_prop("id", AAZStrType, ".remote_vnet")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.etag = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.id = AAZStrType()
            _schema_on_200_201.name = AAZStrType()
            _schema_on_200_201.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200_201.type = AAZStrType()

            properties = cls._schema_on_200_201.properties
            properties.allow_forwarded_traffic = AAZBoolType(
                serialized_name="allowForwardedTraffic",
            )
            properties.allow_gateway_transit = AAZBoolType(
                serialized_name="allowGatewayTransit",
            )
            properties.allow_virtual_network_access = AAZBoolType(
                serialized_name="allowVirtualNetworkAccess",
            )
            properties.do_not_verify_remote_gateways = AAZBoolType(
                serialized_name="doNotVerifyRemoteGateways",
            )
            properties.enable_only_i_pv6_peering = AAZBoolType(
                serialized_name="enableOnlyIPv6Peering",
            )
            properties.local_address_space = AAZObjectType(
                serialized_name="localAddressSpace",
            )
            _CreateHelper._build_schema_address_space_read(properties.local_address_space)
            properties.local_subnet_names = AAZListType(
                serialized_name="localSubnetNames",
            )
            properties.local_virtual_network_address_space = AAZObjectType(
                serialized_name="localVirtualNetworkAddressSpace",
            )
            _CreateHelper._build_schema_address_space_read(properties.local_virtual_network_address_space)
            properties.peer_complete_vnets = AAZBoolType(
                serialized_name="peerCompleteVnets",
            )
            properties.peering_state = AAZStrType(
                serialized_name="peeringState",
            )
            properties.peering_sync_level = AAZStrType(
                serialized_name="peeringSyncLevel",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.remote_address_space = AAZObjectType(
                serialized_name="remoteAddressSpace",
            )
            _CreateHelper._build_schema_address_space_read(properties.remote_address_space)
            properties.remote_bgp_communities = AAZObjectType(
                serialized_name="remoteBgpCommunities",
            )
            properties.remote_subnet_names = AAZListType(
                serialized_name="remoteSubnetNames",
            )
            properties.remote_virtual_network = AAZObjectType(
                serialized_name="remoteVirtualNetwork",
            )
            properties.remote_virtual_network_address_space = AAZObjectType(
                serialized_name="remoteVirtualNetworkAddressSpace",
            )
            _CreateHelper._build_schema_address_space_read(properties.remote_virtual_network_address_space)
            properties.remote_virtual_network_encryption = AAZObjectType(
                serialized_name="remoteVirtualNetworkEncryption",
            )
            properties.resource_guid = AAZStrType(
                serialized_name="resourceGuid",
                flags={"read_only": True},
            )
            properties.use_remote_gateways = AAZBoolType(
                serialized_name="useRemoteGateways",
            )

            local_subnet_names = cls._schema_on_200_201.properties.local_subnet_names
            local_subnet_names.Element = AAZStrType()

            remote_bgp_communities = cls._schema_on_200_201.properties.remote_bgp_communities
            remote_bgp_communities.regional_community = AAZStrType(
                serialized_name="regionalCommunity",
                flags={"read_only": True},
            )
            remote_bgp_communities.virtual_network_community = AAZStrType(
                serialized_name="virtualNetworkCommunity",
                flags={"required": True},
            )

            remote_subnet_names = cls._schema_on_200_201.properties.remote_subnet_names
            remote_subnet_names.Element = AAZStrType()

            remote_virtual_network = cls._schema_on_200_201.properties.remote_virtual_network
            remote_virtual_network.id = AAZStrType()

            remote_virtual_network_encryption = cls._schema_on_200_201.properties.remote_virtual_network_encryption
            remote_virtual_network_encryption.enabled = AAZBoolType(
                flags={"required": True},
            )
            remote_virtual_network_encryption.enforcement = AAZStrType()

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""

    @classmethod
    def _build_schema_address_space_create(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("addressPrefixes", AAZListType, ".address_prefixes")

        address_prefixes = _builder.get(".addressPrefixes")
        if address_prefixes is not None:
            address_prefixes.set_elements(AAZStrType, ".")

    _schema_address_space_read = None

    @classmethod
    def _build_schema_address_space_read(cls, _schema):
        if cls._schema_address_space_read is not None:
            _schema.address_prefixes = cls._schema_address_space_read.address_prefixes
            return

        cls._schema_address_space_read = _schema_address_space_read = AAZObjectType()

        address_space_read = _schema_address_space_read
        address_space_read.address_prefixes = AAZListType(
            serialized_name="addressPrefixes",
        )

        address_prefixes = _schema_address_space_read.address_prefixes
        address_prefixes.Element = AAZStrType()

        _schema.address_prefixes = cls._schema_address_space_read.address_prefixes


__all__ = ["Create"]
