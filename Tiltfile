analytics_settings(False)

load('ext://uibutton', 'cmd_button', 'location')

allow_k8s_contexts('imac')

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

k8s_yaml(kustomize('k'))