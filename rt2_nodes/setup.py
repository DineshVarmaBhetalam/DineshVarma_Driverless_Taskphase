from setuptools import find_packages, setup

package_name = 'rt2_nodes'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dineshvarmab',
    maintainer_email='dinesh.mitmpl2026@learner.manipal.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
                'node1 = rt2_nodes.node1_publisher:main',
                'node2 = rt2_nodes.node2_checker:main',
                'node3 = rt2_nodes.node3_responder:main',
        ],
    },
)
