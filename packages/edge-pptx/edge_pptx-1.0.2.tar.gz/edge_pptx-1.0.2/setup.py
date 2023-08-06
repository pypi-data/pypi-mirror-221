from setuptools import setup
import io
with io.open('README.MD', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='edge_pptx',
    version='1.0.2',
    packages=['ppt_style'],
    url='https://github.com/edgeriver/PPTX_edge.git',
    license='MIT',
    author='wangwl',
    author_email='643176574@qq.com',
    description='用于生成 PowerPoint 文件的 Python 模块',
    python_requires='>=3.6, <=3.12',
    install_requires=["requests==2.31.0", "python-pptx==0.6.21"],
    package_data={'ppt_style': ['templates/default.pptx']},
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Intended Audience :: Developers',        # 预期的受众
        'Topic :: Software Development :: Libraries :: Python Modules',  # 主题和领域
    ],

)
