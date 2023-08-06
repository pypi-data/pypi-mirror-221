import click
from case_project.main_fun import get_version


@click.command()
@click.option('-v', '--version', help='版本, 当前--key/--name', is_eager=True, is_flag=True)
@click.option('-k', '--key', help='项目key, 传*表示所有项目，不传默认去上一次key', multiple=True)
@click.option('-n', '--name', help='项目名称, 传*表示所有项目，不传默认去上一次name', multiple=True)
@click.option('-i', '--install', help='根据key创建项目, 项目存在则更新')
@click.option('-u', '--update', help='根据--key更新项目，--key不存在时默认取之前的值', is_eager=True, is_flag=True)
@click.option('-f', '--fun', help='新增api方法，参数url，--key不存在时默认取之前的值', multiple=True)
def main(version, key, name, install, update, fun):
    print(version, key, name, install, update, fun)
    if version:
        click.echo(get_version())
    #
    # for k in key:
    #     if install:
    #         click.echo('init：' + _version)
    #         click.echo(type(install))
    #     elif update:
    #         click.echo('update：' + _version)
    #         click.echo(type(update))


if __name__ == '__main__':
    main()