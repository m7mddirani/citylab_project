from launch import LaunchDescription
import launch_ros.actions

def generate_launch_description():
    # Set parameters for the patrol node
    patrol_params = {
        'kp': 0.35,  # Proportional gain for angular velocity
        'safety_margin': 0.25  # Minimum safe distance from obstacles
    }

    # Create node for the patrol behavior
    patrol_node = launch_ros.actions.Node(
        package='robot_patrol', 
        executable='patrol',
        output='screen',
        parameters=[patrol_params]
    )

    return LaunchDescription([
        patrol_node
    ])