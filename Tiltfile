analytics_settings(False)

k8s_yaml(kustomize('k'))

docker_build('hanbaiki', '.',
  live_update=[
    sync('.', '/app'),
  ]
)
