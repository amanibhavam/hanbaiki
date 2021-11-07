analytics_settings(False)

k8s_yaml(kustomize('k'))

docker_build('hanbaiki', 'front',
  live_update=[
    sync('front', '/app'),
  ]
)
