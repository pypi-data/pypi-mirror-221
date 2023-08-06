from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/management-security.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_management_security = resolve('management_security')
    try:
        t_1 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_2 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_2((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security)):
        pass
        yield '!\nmanagement security\n'
        if t_2(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'entropy_source')):
            pass
            yield '   entropy source '
            yield str(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'entropy_source'))
            yield '\n'
        if t_2(environment.getattr(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'password'), 'encryption_key_common'), True):
            pass
            yield '   password encryption-key common\n'
        if t_2(environment.getattr(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'password'), 'encryption_reversible')):
            pass
            yield '   password encryption reversible '
            yield str(environment.getattr(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'password'), 'encryption_reversible'))
            yield '\n'
        if t_2(environment.getattr(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'password'), 'minimum_length')):
            pass
            yield '   password minimum length '
            yield str(environment.getattr(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'password'), 'minimum_length'))
            yield '\n'
        if t_2(environment.getattr(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'password'), 'policies')):
            pass
            for l_1_policy in environment.getattr(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'password'), 'policies'):
                _loop_vars = {}
                pass
                yield '   password policy '
                yield str(environment.getattr(l_1_policy, 'name'))
                yield '\n'
                if t_2(environment.getattr(l_1_policy, 'minimum')):
                    pass
                    if t_2(environment.getattr(environment.getattr(l_1_policy, 'minimum'), 'digits')):
                        pass
                        yield '      minimum digits '
                        yield str(environment.getattr(environment.getattr(l_1_policy, 'minimum'), 'digits'))
                        yield '\n'
                    if t_2(environment.getattr(environment.getattr(l_1_policy, 'minimum'), 'length')):
                        pass
                        yield '      minimum length '
                        yield str(environment.getattr(environment.getattr(l_1_policy, 'minimum'), 'length'))
                        yield '\n'
                    if t_2(environment.getattr(environment.getattr(l_1_policy, 'minimum'), 'lower')):
                        pass
                        yield '      minimum lower '
                        yield str(environment.getattr(environment.getattr(l_1_policy, 'minimum'), 'lower'))
                        yield '\n'
                    if t_2(environment.getattr(environment.getattr(l_1_policy, 'minimum'), 'special')):
                        pass
                        yield '      minimum special '
                        yield str(environment.getattr(environment.getattr(l_1_policy, 'minimum'), 'special'))
                        yield '\n'
                    if t_2(environment.getattr(environment.getattr(l_1_policy, 'minimum'), 'upper')):
                        pass
                        yield '      minimum upper '
                        yield str(environment.getattr(environment.getattr(l_1_policy, 'minimum'), 'upper'))
                        yield '\n'
                if t_2(environment.getattr(l_1_policy, 'maximum')):
                    pass
                    if t_2(environment.getattr(environment.getattr(l_1_policy, 'maximum'), 'repetitive')):
                        pass
                        yield '      maximum repetitive '
                        yield str(environment.getattr(environment.getattr(l_1_policy, 'maximum'), 'repetitive'))
                        yield '\n'
                    if t_2(environment.getattr(environment.getattr(l_1_policy, 'maximum'), 'sequential')):
                        pass
                        yield '      maximum sequential '
                        yield str(environment.getattr(environment.getattr(l_1_policy, 'maximum'), 'sequential'))
                        yield '\n'
            l_1_policy = missing
        for l_1_ssl_profile in t_1(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'ssl_profiles')):
            _loop_vars = {}
            pass
            yield '   ssl profile '
            yield str(environment.getattr(l_1_ssl_profile, 'name'))
            yield '\n'
            if t_2(environment.getattr(l_1_ssl_profile, 'tls_versions')):
                pass
                yield '      tls versions '
                yield str(environment.getattr(l_1_ssl_profile, 'tls_versions'))
                yield '\n'
            if t_2(environment.getattr(l_1_ssl_profile, 'cipher_list')):
                pass
                yield '      cipher-list '
                yield str(environment.getattr(l_1_ssl_profile, 'cipher_list'))
                yield '\n'
            if t_2(environment.getattr(l_1_ssl_profile, 'trust_certificate')):
                pass
                for l_2_trust_cert in t_1(environment.getattr(environment.getattr(l_1_ssl_profile, 'trust_certificate'), 'certificates')):
                    _loop_vars = {}
                    pass
                    yield '      trust certificate '
                    yield str(l_2_trust_cert)
                    yield '\n'
                l_2_trust_cert = missing
                if t_2(environment.getattr(environment.getattr(l_1_ssl_profile, 'trust_certificate'), 'system'), True):
                    pass
                    yield '      trust certificate system\n'
                if t_2(environment.getattr(environment.getattr(l_1_ssl_profile, 'trust_certificate'), 'requirement')):
                    pass
                    if t_2(environment.getattr(environment.getattr(environment.getattr(l_1_ssl_profile, 'trust_certificate'), 'requirement'), 'basic_constraint_ca'), True):
                        pass
                        yield '      trust certificate requirement basic-constraint ca true\n'
                    if t_2(environment.getattr(environment.getattr(environment.getattr(l_1_ssl_profile, 'trust_certificate'), 'requirement'), 'hostname_fqdn'), True):
                        pass
                        yield '      trust certificate requirement hostname fqdn\n'
                if t_2(environment.getattr(environment.getattr(l_1_ssl_profile, 'trust_certificate'), 'policy_expiry_date_ignore'), True):
                    pass
                    yield '      trust certificate policy expiry-date ignore\n'
            if t_2(environment.getattr(l_1_ssl_profile, 'chain_certificate')):
                pass
                for l_2_chain_cert in t_1(environment.getattr(environment.getattr(l_1_ssl_profile, 'chain_certificate'), 'certificates')):
                    _loop_vars = {}
                    pass
                    yield '      chain certificate '
                    yield str(l_2_chain_cert)
                    yield '\n'
                l_2_chain_cert = missing
                if t_2(environment.getattr(environment.getattr(l_1_ssl_profile, 'chain_certificate'), 'requirement')):
                    pass
                    if t_2(environment.getattr(environment.getattr(environment.getattr(l_1_ssl_profile, 'chain_certificate'), 'requirement'), 'basic_constraint_ca'), True):
                        pass
                        yield '      chain certificate requirement basic-constraint ca true\n'
                    if t_2(environment.getattr(environment.getattr(environment.getattr(l_1_ssl_profile, 'chain_certificate'), 'requirement'), 'include_root_ca'), True):
                        pass
                        yield '      chain certificate requirement include root-ca\n'
            if t_2(environment.getattr(l_1_ssl_profile, 'certificate')):
                pass
                yield '      certificate '
                yield str(environment.getattr(environment.getattr(l_1_ssl_profile, 'certificate'), 'file'))
                yield ' key '
                yield str(environment.getattr(environment.getattr(l_1_ssl_profile, 'certificate'), 'key'))
                yield '\n'
        l_1_ssl_profile = missing

blocks = {}
debug_info = '2=24&5=27&6=30&8=32&11=35&12=38&14=40&15=43&17=45&18=47&19=51&20=53&21=55&22=58&24=60&25=63&27=65&28=68&30=70&31=73&33=75&34=78&37=80&38=82&39=85&41=87&42=90&47=93&48=97&49=99&50=102&52=104&53=107&55=109&56=111&57=115&59=118&62=121&63=123&66=126&70=129&74=132&75=134&76=138&78=141&79=143&82=146&87=149&88=152'