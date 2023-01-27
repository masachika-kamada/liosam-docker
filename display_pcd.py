import sys
import open3d as o3d


def read_pcd(file_path):
    return o3d.io.read_point_cloud(file_path)


def kdtree(radius, max_nn):
    return o3d.geometry.KDTreeSearchParamHybrid(radius=radius, max_nn=max_nn)


def draw_pcd(pcd, window_name="Open3D"):
    pcd.paint_uniform_color([0, 1, 0])
    pcd.estimate_normals(kdtree(radius=1, max_nn=30))
    o3d.visualization.draw_geometries([pcd], window_name=window_name)


def main():
    pcd = read_pcd(sys.argv[1])
    draw_pcd(pcd)


if __name__ == "__main__":
    main()
