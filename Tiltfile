analytics_settings(False)

k8s_yaml(kustomize('k'))

docker_build('hanbaiki', 'web',
  live_update=[
    sync('web', '/app'),
  ]
)

docker_build('hanbaiki-web', 'web/dist',
  live_update=[
    sync('web/dist', '/usr/share/nginx/html'),
  ]
)

docker_build('hanbaiki-api', 'api',
  live_update=[
    sync('api', '/app'),
  ]
)

load('ext://uibutton', 'cmd_button', 'location')

cmd_button(name='build for web',
          icon_name='build',
          resource='hanbaiki',
          argv=['bin/chdir-exec', 'web', 'vite', 'build'])
