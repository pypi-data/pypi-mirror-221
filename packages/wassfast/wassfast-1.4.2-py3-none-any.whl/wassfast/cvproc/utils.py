import numpy as np
import cv2 as cv


def load_ocv_matrix( filename ):
    fs_read = cv.FileStorage( filename, cv.FILE_STORAGE_READ)
    arr_read = fs_read.getFirstTopLevelNode().mat()      
    fs_read.release()
    return arr_read


# Debug extracted features in plane space
def debug_featuresP( matcher, I0p, I1p, outdir="dbg/", cam0name="cam0P_features", cam1name="cam1P_features" ):
    I0p_aux = cv.cvtColor( I0p, cv.COLOR_GRAY2BGR )

    for idx in range(0,matcher.features_0P_all.shape[0]):
        cv.drawMarker(I0p_aux, tuple( matcher.features_0P_all[idx,:] ), (0,0,0), markerType=cv.MARKER_TILTED_CROSS, markerSize=5  )

    for idx in range(0,matcher.features_0P.shape[0]):
        cv.drawMarker(I0p_aux, tuple( matcher.features_0P[idx,:] ), (0,0,255), markerType=cv.MARKER_TILTED_CROSS, markerSize=5  )
    
    cv.imwrite("%s/%s.jpg"%(outdir,cam0name), I0p_aux)

    I1p_aux = cv.cvtColor( I1p, cv.COLOR_GRAY2BGR )
    f1_int = np.round(matcher.features_1P)
    for idx in range(0,f1_int.shape[0]):
        cv.drawMarker(I1p_aux, tuple( f1_int[idx,:] ), (0,0,255), markerType=cv.MARKER_TILTED_CROSS, markerSize=5  )

    cv.imwrite("%s/%s.jpg"%(outdir,cam1name), I1p_aux)


# Debug features in camera space
def debug_features( I0, I1, features_0, features_1, outdir="dbg/"):
    I0_aux = cv.cvtColor( I0, cv.COLOR_GRAY2BGR )
    f0_int = np.round(features_0).astype(np.uint32)
    for idx in range(0,f0_int.shape[1]):
        cv.drawMarker(I0_aux, tuple( f0_int[:,idx] ), (255,0,0), markerType=cv.MARKER_TILTED_CROSS, markerSize=10  )
    cv.imwrite("%s/cam0_features.jpg"%outdir, I0_aux)

    I1_aux = cv.cvtColor( I1, cv.COLOR_GRAY2BGR )
    f1_int = np.round(features_1).astype(np.uint32)
    for idx in range(0,f1_int.shape[1]):
        cv.drawMarker(I1_aux, tuple( f1_int[:,idx] ), (255,0,0), markerType=cv.MARKER_TILTED_CROSS, markerSize=10  )
    cv.imwrite("%s/cam1_features.jpg"%outdir, I1_aux)


def debug_area( I0, I1, I0pshape, c2sH_cam0, c2sH_cam1, outdir="dbg/", line_thickness=10 ):
    area_extent_pts = np.array([ [0,0], [I0pshape[1],0], [I0pshape[1],I0pshape[0]] , [0, I0pshape[0]] ], dtype=np.float32  )
    area_extent_pts0 = c2sH_cam0.transform( area_extent_pts.T, inverse=True ).astype(np.int32)
    area_extent_pts1 = c2sH_cam1.transform( area_extent_pts.T, inverse=True ).astype(np.int32)

    I0_aux = cv.cvtColor( I0, cv.COLOR_GRAY2BGR )
    I1_aux = cv.cvtColor( I1, cv.COLOR_GRAY2BGR )
    for ii in range(4):
        cv.line( I0_aux, (area_extent_pts0[0][ii],area_extent_pts0[1][ii]), (area_extent_pts0[0][(ii+1)%4],area_extent_pts0[1][(ii+1)%4]), (0,0,255), line_thickness ) 
        cv.line( I1_aux, (area_extent_pts1[0][ii],area_extent_pts1[1][ii]), (area_extent_pts1[0][(ii+1)%4],area_extent_pts1[1][(ii+1)%4]), (0,0,255), line_thickness ) 

    cv.imwrite("%s/cam0_area.jpg"%outdir, I0_aux)
    cv.imwrite("%s/cam1_area.jpg"%outdir, I1_aux)