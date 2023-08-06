from setuptools import setup, find_packages

setup(
    name='simple music tools',
    version='0.1.0',
    packages=find_packages(include=['dist', 'dist.*']),
    license='Apache License 2.0',
    description='A simple set of music analysis tools based on Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Steve Yi',
    # install_requires=['numpy'],  # 这个包的依赖项，例如，numpy
    # url='http://github.com/yourusername/your-package-name',  # 你的项目的github链接或者其他的链接
    # long_description_content_type='text/markdown',  # 长描述的内容类型，设置为markdown
    # author_email='your.email@example.com',  # 你的邮箱
)
