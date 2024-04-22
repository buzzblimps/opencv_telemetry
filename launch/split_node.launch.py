import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'namespace',
            default_value='MaryO',
            description='Namespace for the node'
        ),
        DeclareLaunchArgument(
            'calibration_file',
            default_value='camera1',
            description='Name of the package containing calibration files'
        ),
        Node(
            package='opencv_telemetry',
            executable='split_sync_images',
            namespace=LaunchConfiguration('namespace'),
            name='split_sync_image_node',
            parameters=[
                {'calibration_file': LaunchConfiguration('calibration_file')},
            ],
        ),
  ])
