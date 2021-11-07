analytics_settings(False)

k8s_yaml(kustomize('k'))

docker_build('hanbaiki', 'front',
  live_update=[
    sync('front', '/app'),
  ]
)

docker_build('hanbaiki-dist', 'front',
  dockerfile='front/Dockerfile.dist',
  live_update=[
    sync('front/dist', '/usr/share/nginx/html'),
  ]
)
