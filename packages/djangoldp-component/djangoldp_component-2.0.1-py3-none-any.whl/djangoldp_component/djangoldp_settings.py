# override authentication backends at package level
AUTHENTICATION_BACKENDS = [
    'djangoldp_component.auth.backends.BasicAuthBackend'
]