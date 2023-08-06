from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/snmp-server.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_snmp_server = resolve('snmp_server')
    try:
        t_1 = environment.filters['arista.avd.default']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.default' found.")
    try:
        t_2 = environment.filters['arista.avd.hide_passwords']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.hide_passwords' found.")
    try:
        t_3 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_4 = environment.filters['string']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No filter named 'string' found.")
    try:
        t_5 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_5(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_5((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server)):
        pass
        yield '!\n'
        if t_5(environment.getattr(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'engine_ids'), 'local')):
            pass
            yield 'snmp-server engineID local '
            yield str(environment.getattr(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'engine_ids'), 'local'))
            yield '\n'
        if t_5(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'contact')):
            pass
            yield 'snmp-server contact '
            yield str(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'contact'))
            yield '\n'
        if t_5(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'location')):
            pass
            yield 'snmp-server location '
            yield str(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'location'))
            yield '\n'
        if t_5(environment.getattr(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'engine_ids'), 'remotes')):
            pass
            for l_1_engine_id in environment.getattr(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'engine_ids'), 'remotes'):
                l_1_remote_engine_ids_cli = resolve('remote_engine_ids_cli')
                _loop_vars = {}
                pass
                if (t_5(environment.getattr(l_1_engine_id, 'id')) and t_5(environment.getattr(l_1_engine_id, 'address'))):
                    pass
                    l_1_remote_engine_ids_cli = str_join(('snmp-server engineID remote ', environment.getattr(l_1_engine_id, 'address'), ))
                    _loop_vars['remote_engine_ids_cli'] = l_1_remote_engine_ids_cli
                    if t_5(environment.getattr(l_1_engine_id, 'udp_port')):
                        pass
                        l_1_remote_engine_ids_cli = str_join(((undefined(name='remote_engine_ids_cli') if l_1_remote_engine_ids_cli is missing else l_1_remote_engine_ids_cli), ' udp-port ', environment.getattr(l_1_engine_id, 'udp_port'), ))
                        _loop_vars['remote_engine_ids_cli'] = l_1_remote_engine_ids_cli
                    l_1_remote_engine_ids_cli = str_join(((undefined(name='remote_engine_ids_cli') if l_1_remote_engine_ids_cli is missing else l_1_remote_engine_ids_cli), ' ', environment.getattr(l_1_engine_id, 'id'), ))
                    _loop_vars['remote_engine_ids_cli'] = l_1_remote_engine_ids_cli
                    yield str((undefined(name='remote_engine_ids_cli') if l_1_remote_engine_ids_cli is missing else l_1_remote_engine_ids_cli))
                    yield '\n'
            l_1_engine_id = l_1_remote_engine_ids_cli = missing
        if t_5(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'ipv4_acls')):
            pass
            for l_1_acl in environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'ipv4_acls'):
                l_1_acl_cli = missing
                _loop_vars = {}
                pass
                l_1_acl_cli = str_join(('snmp-server ipv4 access-list ', environment.getattr(l_1_acl, 'name'), ))
                _loop_vars['acl_cli'] = l_1_acl_cli
                if t_5(environment.getattr(l_1_acl, 'vrf')):
                    pass
                    l_1_acl_cli = str_join(((undefined(name='acl_cli') if l_1_acl_cli is missing else l_1_acl_cli), ' vrf ', environment.getattr(l_1_acl, 'vrf'), ))
                    _loop_vars['acl_cli'] = l_1_acl_cli
                yield str((undefined(name='acl_cli') if l_1_acl_cli is missing else l_1_acl_cli))
                yield '\n'
            l_1_acl = l_1_acl_cli = missing
        if t_5(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'ipv6_acls')):
            pass
            for l_1_acl in environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'ipv6_acls'):
                l_1_acl_cli = missing
                _loop_vars = {}
                pass
                l_1_acl_cli = str_join(('snmp-server ipv6 access-list ', environment.getattr(l_1_acl, 'name'), ))
                _loop_vars['acl_cli'] = l_1_acl_cli
                if t_5(environment.getattr(l_1_acl, 'vrf')):
                    pass
                    l_1_acl_cli = str_join(((undefined(name='acl_cli') if l_1_acl_cli is missing else l_1_acl_cli), ' vrf ', environment.getattr(l_1_acl, 'vrf'), ))
                    _loop_vars['acl_cli'] = l_1_acl_cli
                yield str((undefined(name='acl_cli') if l_1_acl_cli is missing else l_1_acl_cli))
                yield '\n'
            l_1_acl = l_1_acl_cli = missing
        if t_5(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'local_interfaces')):
            pass
            for l_1_local_interface in environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'local_interfaces'):
                l_1_interface_snmp_cli = missing
                _loop_vars = {}
                pass
                l_1_interface_snmp_cli = 'snmp-server'
                _loop_vars['interface_snmp_cli'] = l_1_interface_snmp_cli
                if t_5(environment.getattr(l_1_local_interface, 'vrf')):
                    pass
                    l_1_interface_snmp_cli = str_join(((undefined(name='interface_snmp_cli') if l_1_interface_snmp_cli is missing else l_1_interface_snmp_cli), ' vrf ', environment.getattr(l_1_local_interface, 'vrf'), ))
                    _loop_vars['interface_snmp_cli'] = l_1_interface_snmp_cli
                l_1_interface_snmp_cli = str_join(((undefined(name='interface_snmp_cli') if l_1_interface_snmp_cli is missing else l_1_interface_snmp_cli), ' local-interface ', environment.getattr(l_1_local_interface, 'name'), ))
                _loop_vars['interface_snmp_cli'] = l_1_interface_snmp_cli
                yield str((undefined(name='interface_snmp_cli') if l_1_interface_snmp_cli is missing else l_1_interface_snmp_cli))
                yield '\n'
            l_1_local_interface = l_1_interface_snmp_cli = missing
        if t_5(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'views')):
            pass
            for l_1_view in environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'views'):
                l_1_view_cli = resolve('view_cli')
                _loop_vars = {}
                pass
                if t_5(environment.getattr(l_1_view, 'name')):
                    pass
                    l_1_view_cli = str_join(('snmp-server view ', environment.getattr(l_1_view, 'name'), ))
                    _loop_vars['view_cli'] = l_1_view_cli
                if t_5(t_1(environment.getattr(l_1_view, 'mib_family_name'), environment.getattr(l_1_view, 'MIB_family_name'))):
                    pass
                    l_1_view_cli = str_join(((undefined(name='view_cli') if l_1_view_cli is missing else l_1_view_cli), ' ', t_1(environment.getattr(l_1_view, 'mib_family_name'), environment.getattr(l_1_view, 'MIB_family_name')), ))
                    _loop_vars['view_cli'] = l_1_view_cli
                if t_5(environment.getattr(l_1_view, 'included'), True):
                    pass
                    l_1_view_cli = str_join(((undefined(name='view_cli') if l_1_view_cli is missing else l_1_view_cli), ' included', ))
                    _loop_vars['view_cli'] = l_1_view_cli
                elif t_5(environment.getattr(l_1_view, 'included'), False):
                    pass
                    l_1_view_cli = str_join(((undefined(name='view_cli') if l_1_view_cli is missing else l_1_view_cli), ' excluded', ))
                    _loop_vars['view_cli'] = l_1_view_cli
                yield str((undefined(name='view_cli') if l_1_view_cli is missing else l_1_view_cli))
                yield '\n'
            l_1_view = l_1_view_cli = missing
        if t_5(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'communities')):
            pass
            for l_1_community in t_3(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'communities'), 'name'):
                l_1_hide_passwords = resolve('hide_passwords')
                l_1_communities_cli = missing
                _loop_vars = {}
                pass
                l_1_communities_cli = str_join(('snmp-server community ', t_2(environment.getattr(l_1_community, 'name'), (undefined(name='hide_passwords') if l_1_hide_passwords is missing else l_1_hide_passwords)), ))
                _loop_vars['communities_cli'] = l_1_communities_cli
                if t_5(environment.getattr(l_1_community, 'view')):
                    pass
                    l_1_communities_cli = str_join(((undefined(name='communities_cli') if l_1_communities_cli is missing else l_1_communities_cli), ' view ', environment.getattr(l_1_community, 'view'), ))
                    _loop_vars['communities_cli'] = l_1_communities_cli
                if t_5(environment.getattr(l_1_community, 'access')):
                    pass
                    l_1_communities_cli = str_join(((undefined(name='communities_cli') if l_1_communities_cli is missing else l_1_communities_cli), ' ', environment.getattr(l_1_community, 'access'), ))
                    _loop_vars['communities_cli'] = l_1_communities_cli
                else:
                    pass
                    l_1_communities_cli = str_join(((undefined(name='communities_cli') if l_1_communities_cli is missing else l_1_communities_cli), ' ro', ))
                    _loop_vars['communities_cli'] = l_1_communities_cli
                if t_5(environment.getattr(l_1_community, 'access_list_ipv6')):
                    pass
                    l_1_communities_cli = str_join(((undefined(name='communities_cli') if l_1_communities_cli is missing else l_1_communities_cli), ' ipv6 ', environment.getattr(environment.getattr(l_1_community, 'access_list_ipv6'), 'name'), ))
                    _loop_vars['communities_cli'] = l_1_communities_cli
                if t_5(environment.getattr(l_1_community, 'access_list_ipv4')):
                    pass
                    l_1_communities_cli = str_join(((undefined(name='communities_cli') if l_1_communities_cli is missing else l_1_communities_cli), ' ', environment.getattr(environment.getattr(l_1_community, 'access_list_ipv4'), 'name'), ))
                    _loop_vars['communities_cli'] = l_1_communities_cli
                yield str((undefined(name='communities_cli') if l_1_communities_cli is missing else l_1_communities_cli))
                yield '\n'
            l_1_community = l_1_hide_passwords = l_1_communities_cli = missing
        if t_5(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'groups')):
            pass
            for l_1_group in environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'groups'):
                l_1_group_cli = resolve('group_cli')
                _loop_vars = {}
                pass
                if t_5(environment.getattr(l_1_group, 'name')):
                    pass
                    l_1_group_cli = str_join(('snmp-server group ', environment.getattr(l_1_group, 'name'), ))
                    _loop_vars['group_cli'] = l_1_group_cli
                if t_5(environment.getattr(l_1_group, 'version')):
                    pass
                    l_1_group_cli = str_join(((undefined(name='group_cli') if l_1_group_cli is missing else l_1_group_cli), ' ', environment.getattr(l_1_group, 'version'), ))
                    _loop_vars['group_cli'] = l_1_group_cli
                if (t_5(environment.getattr(l_1_group, 'authentication')) and t_5(environment.getattr(l_1_group, 'version'), 'v3')):
                    pass
                    l_1_group_cli = str_join(((undefined(name='group_cli') if l_1_group_cli is missing else l_1_group_cli), ' ', environment.getattr(l_1_group, 'authentication'), ))
                    _loop_vars['group_cli'] = l_1_group_cli
                if t_5(environment.getattr(l_1_group, 'read')):
                    pass
                    l_1_group_cli = str_join(((undefined(name='group_cli') if l_1_group_cli is missing else l_1_group_cli), ' read ', environment.getattr(l_1_group, 'read'), ))
                    _loop_vars['group_cli'] = l_1_group_cli
                if t_5(environment.getattr(l_1_group, 'write')):
                    pass
                    l_1_group_cli = str_join(((undefined(name='group_cli') if l_1_group_cli is missing else l_1_group_cli), ' write ', environment.getattr(l_1_group, 'write'), ))
                    _loop_vars['group_cli'] = l_1_group_cli
                if t_5(environment.getattr(l_1_group, 'notify')):
                    pass
                    l_1_group_cli = str_join(((undefined(name='group_cli') if l_1_group_cli is missing else l_1_group_cli), ' notify ', environment.getattr(l_1_group, 'notify'), ))
                    _loop_vars['group_cli'] = l_1_group_cli
                yield str((undefined(name='group_cli') if l_1_group_cli is missing else l_1_group_cli))
                yield '\n'
            l_1_group = l_1_group_cli = missing
        if t_5(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'users')):
            pass
            for l_1_user in environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'users'):
                l_1_user_cli = resolve('user_cli')
                l_1_hide_passwords = resolve('hide_passwords')
                _loop_vars = {}
                pass
                if t_5(environment.getattr(l_1_user, 'name')):
                    pass
                    l_1_user_cli = str_join(('snmp-server user ', environment.getattr(l_1_user, 'name'), ))
                    _loop_vars['user_cli'] = l_1_user_cli
                if t_5(environment.getattr(l_1_user, 'group')):
                    pass
                    l_1_user_cli = str_join(((undefined(name='user_cli') if l_1_user_cli is missing else l_1_user_cli), ' ', environment.getattr(l_1_user, 'group'), ))
                    _loop_vars['user_cli'] = l_1_user_cli
                if (t_5(environment.getattr(l_1_user, 'remote_address')) and t_5(environment.getattr(l_1_user, 'version'), 'v3')):
                    pass
                    l_1_user_cli = str_join(((undefined(name='user_cli') if l_1_user_cli is missing else l_1_user_cli), ' remote ', environment.getattr(l_1_user, 'remote_address'), ))
                    _loop_vars['user_cli'] = l_1_user_cli
                    if t_5(environment.getattr(l_1_user, 'udp_port')):
                        pass
                        l_1_user_cli = str_join(((undefined(name='user_cli') if l_1_user_cli is missing else l_1_user_cli), ' udp-port ', environment.getattr(l_1_user, 'udp_port'), ))
                        _loop_vars['user_cli'] = l_1_user_cli
                if t_5(environment.getattr(l_1_user, 'version')):
                    pass
                    l_1_user_cli = str_join(((undefined(name='user_cli') if l_1_user_cli is missing else l_1_user_cli), ' ', environment.getattr(l_1_user, 'version'), ))
                    _loop_vars['user_cli'] = l_1_user_cli
                if ((t_5(environment.getattr(l_1_user, 'auth')) and t_5(environment.getattr(l_1_user, 'version'), 'v3')) and t_5(environment.getattr(l_1_user, 'auth_passphrase'))):
                    pass
                    if t_5(environment.getattr(l_1_user, 'localized')):
                        pass
                        l_1_user_cli = str_join(((undefined(name='user_cli') if l_1_user_cli is missing else l_1_user_cli), ' localized ', environment.getattr(l_1_user, 'localized'), ))
                        _loop_vars['user_cli'] = l_1_user_cli
                    l_1_user_cli = str_join(((undefined(name='user_cli') if l_1_user_cli is missing else l_1_user_cli), ' auth ', environment.getattr(l_1_user, 'auth'), ' ', t_2(environment.getattr(l_1_user, 'auth_passphrase'), (undefined(name='hide_passwords') if l_1_hide_passwords is missing else l_1_hide_passwords)), ))
                    _loop_vars['user_cli'] = l_1_user_cli
                    if (t_5(environment.getattr(l_1_user, 'priv')) and t_5(environment.getattr(l_1_user, 'priv_passphrase'))):
                        pass
                        l_1_user_cli = str_join(((undefined(name='user_cli') if l_1_user_cli is missing else l_1_user_cli), ' priv ', environment.getattr(l_1_user, 'priv'), ' ', t_2(environment.getattr(l_1_user, 'priv_passphrase'), (undefined(name='hide_passwords') if l_1_hide_passwords is missing else l_1_hide_passwords)), ))
                        _loop_vars['user_cli'] = l_1_user_cli
                yield str((undefined(name='user_cli') if l_1_user_cli is missing else l_1_user_cli))
                yield '\n'
            l_1_user = l_1_user_cli = l_1_hide_passwords = missing
        if t_5(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'hosts')):
            pass
            for l_1_host in environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'hosts'):
                l_1_host_cli = resolve('host_cli')
                l_1_hide_passwords = resolve('hide_passwords')
                _loop_vars = {}
                pass
                if t_5(environment.getattr(l_1_host, 'host')):
                    pass
                    l_1_host_cli = str_join(('snmp-server host ', environment.getattr(l_1_host, 'host'), ))
                    _loop_vars['host_cli'] = l_1_host_cli
                    if t_5(environment.getattr(l_1_host, 'vrf')):
                        pass
                        l_1_host_cli = str_join(((undefined(name='host_cli') if l_1_host_cli is missing else l_1_host_cli), ' vrf ', environment.getattr(l_1_host, 'vrf'), ))
                        _loop_vars['host_cli'] = l_1_host_cli
                    if (t_5(environment.getattr(l_1_host, 'users')) and (t_4(t_1(environment.getattr(l_1_host, 'version'), '3')) == '3')):
                        pass
                        for l_2_user in environment.getattr(l_1_host, 'users'):
                            _loop_vars = {}
                            pass
                            if (t_5(environment.getattr(l_2_user, 'username')) and t_5(environment.getattr(l_2_user, 'authentication_level'))):
                                pass
                                yield str((undefined(name='host_cli') if l_1_host_cli is missing else l_1_host_cli))
                                yield ' version 3 '
                                yield str(environment.getattr(l_2_user, 'authentication_level'))
                                yield ' '
                                yield str(environment.getattr(l_2_user, 'username'))
                                yield '\n'
                        l_2_user = missing
                    elif (t_5(environment.getattr(l_1_host, 'community')) and (t_4(t_1(environment.getattr(l_1_host, 'version'), '2c')) in ['1', '2c'])):
                        pass
                        yield str((undefined(name='host_cli') if l_1_host_cli is missing else l_1_host_cli))
                        yield ' version '
                        yield str(t_1(environment.getattr(l_1_host, 'version'), '2c'))
                        yield ' '
                        yield str(t_2(environment.getattr(l_1_host, 'community'), (undefined(name='hide_passwords') if l_1_hide_passwords is missing else l_1_hide_passwords)))
                        yield '\n'
            l_1_host = l_1_host_cli = l_1_hide_passwords = missing
        if t_5(environment.getattr(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'traps'), 'enable'), True):
            pass
            yield 'snmp-server enable traps\n'
        elif t_5(environment.getattr(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'traps'), 'enable'), False):
            pass
            yield 'no snmp-server enable traps\n'
        for l_1_snmp_trap in t_3(environment.getattr(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'traps'), 'snmp_traps'), 'name'):
            _loop_vars = {}
            pass
            if t_5(environment.getattr(l_1_snmp_trap, 'enabled'), False):
                pass
                yield 'no snmp-server enable traps '
                yield str(environment.getattr(l_1_snmp_trap, 'name'))
                yield '\n'
            else:
                pass
                yield 'snmp-server enable traps '
                yield str(environment.getattr(l_1_snmp_trap, 'name'))
                yield '\n'
        l_1_snmp_trap = missing
        if t_5(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'vrfs')):
            pass
            for l_1_vrf in environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'vrfs'):
                _loop_vars = {}
                pass
                if t_5(environment.getattr(l_1_vrf, 'enable'), True):
                    pass
                    yield 'snmp-server vrf '
                    yield str(environment.getattr(l_1_vrf, 'name'))
                    yield '\n'
                else:
                    pass
                    yield 'no snmp-server vrf '
                    yield str(environment.getattr(l_1_vrf, 'name'))
                    yield '\n'
            l_1_vrf = missing

blocks = {}
debug_info = '2=42&4=45&5=48&7=50&8=53&10=55&11=58&13=60&14=62&15=66&16=68&17=70&18=72&20=74&21=76&25=79&26=81&27=85&28=87&29=89&31=91&34=94&35=96&36=100&37=102&38=104&40=106&43=109&44=111&45=115&46=117&47=119&49=121&50=123&53=126&54=128&55=132&56=134&58=136&59=138&61=140&62=142&63=144&64=146&66=148&69=151&70=153&71=158&72=160&73=162&75=164&76=166&78=170&80=172&81=174&83=176&84=178&86=180&89=183&90=185&91=189&92=191&94=193&95=195&97=197&98=199&100=201&101=203&103=205&104=207&106=209&107=211&109=213&112=216&113=218&114=223&115=225&117=227&118=229&120=231&121=233&122=235&123=237&126=239&127=241&129=243&132=245&133=247&135=249&136=251&138=253&141=255&144=258&145=260&146=265&147=267&148=269&149=271&151=273&153=275&154=278&156=280&159=287&161=289&166=296&168=299&171=302&172=305&173=308&175=313&178=316&179=318&180=321&181=324&183=329'