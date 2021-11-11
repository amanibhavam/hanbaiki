analytics_settings(False)

allow_k8s_contexts('mini')

k8s_yaml(kustomize('k'))

docker_build('defn/hanbaiki:vue', 'web',
  live_update=[
    sync('web', '/app'),
  ]
)

docker_build('defn/hanbaiki:web', 'web',
  dockerfile='web/Dockerfile.web',
  live_update=[
    sync('web/dist', '/usr/share/nginx/html'),
  ]
)

docker_build('defn/hanbaiki:api', 'api',
  live_update=[
    sync('api', '/app'),
  ]
)

load('ext://uibutton', 'cmd_button', 'location')

cmd_button(name='build for web',
          icon_name='build',
          resource='hanbaiki-vue',
          argv=['bin/chdir-exec', 'web', 'vite', 'build'])
