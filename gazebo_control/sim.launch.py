from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
import os

def generate_launch_description():

    gazebo_ros = FindPackageShare('gazebo_ros').find('gazebo_ros')
    turtlebot3_gazebo = FindPackageShare('turtlebot3_gazebo').find('turtlebot3_gazebo')

    world = os.path.join(
        turtlebot3_gazebo,
        'worlds',
        'turtlebot3_world.world'
    )

    return LaunchDescription([

        # ✅ Proper Gazebo (WITH plugins automatically)
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(gazebo_ros, 'launch', 'gazebo.launch.py')
            ),
            launch_arguments={'world': world}.items()
        ),

        # ✅ Spawn robot (NOW service will exist)
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(gazebo_ros, 'launch', 'spawn_entity.launch.py')
            ),
            launch_arguments={
                'entity': 'burger',
                'file': os.path.join(
                    turtlebot3_gazebo,
                    'models',
                    'turtlebot3_burger',
                    'model.sdf'
                )
            }.items()
        )

    ])