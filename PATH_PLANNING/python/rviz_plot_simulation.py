import rospy
from sailboat_message.msg import WTST_msg
from sailboat_message.msg import PointArray
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped, Point
from visualization_msgs.msg import Marker

marker = Marker()
marker.type = marker.POINTS
marker.action = marker.ADD
marker.pose.orientation.w = 1
marker.scale.x = 4.0
marker.scale.y = 4.0
marker.scale.z = 0.0
marker.color.r = 1.0
marker.color.g = 1.0
marker.color.b = 0
marker.color.a = 0.5


def callback(obs_array):
    marker.points = []
    marker.header = obs_array.header
    marker.header.frame_id = 'world'

    target_x = [0]
    target_y = [0]
    for i, pt in enumerate(obs_array.points):
        target_x.append(pt.y)
        target_y.append(pt.x)
        print('obs_{}: {}, {}'.format(i, pt.x, pt.y))

    for xx, yy in zip(target_x, target_y):
        p = Point()
        p.x = xx
        p.y = yy
        marker.points.append(p)

    points_pub.publish(marker)


def main():
    global path_pub, points_pub
    rospy.init_node('path_planning_plot', anonymous=True)
    points_pub = rospy.Publisher('/obs_points', Marker, queue_size=2)

    rospy.Subscriber('/obstacle_coords', PointArray, callback)


if __name__ == '__main__':
    try:
        main()
        rospy.spin()
    except:
        pass