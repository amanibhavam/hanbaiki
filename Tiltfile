analytics_settings(False)

allow_k8s_contexts('imac')

k8s_yaml(kustomize('k'))

docker_build('defn/hanbaiki:web', 'web',
  live_update=[
    sync('web', '/app'),
  ]
)

docker_build('defn/hanbaiki:api', 'api',
  live_update=[
    sync('api', '/app'),
  ]
)

load('ext://uibutton', 'cmd_button', 'location')