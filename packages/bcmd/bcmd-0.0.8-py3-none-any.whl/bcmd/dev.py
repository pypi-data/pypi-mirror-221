import main
from beni import btask

main.init()
btask.options.package = 'tasks'

# btask.dev('db.reset')
# btask.dev('db.backup')
btask.dev('time.showtime', '', '')
# btask.dev('db.clear')
# btask.dev('db.reset_password')
# btask.dev('build.build')
# btask.dev('build_update.run')
# btask.dev('build_main.run')
# btask.dev('build_setup.run')
# btask.dev('db.schema')
# btask.dev('build.build_dev')
# btask.dev('server_code.gen_init')
# btask.dev('maintain.update_version')
