analytics_settings(False)

load('ext://uibutton', 'cmd_button', 'location')

allow_k8s_contexts('imac')

docker_build('defn/hanbaiki:web', 'web',
  build_args={
    "IMAGE": "node:16-buster"
  },
  live_update=[
    sync('web', '/app'),
  ]
)

docker_build('defn/hanbaiki:api', 'api',
  build_args={
    "IMAGE": "registry.mini.defn.ooo:5000/letfn/whoabot:app-0.0.2"
  },
  live_update=[
    sync('api', '/app'),
  ]
)

k8s_yaml(kustomize('k'))