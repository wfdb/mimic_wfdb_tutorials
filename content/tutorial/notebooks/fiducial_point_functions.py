import scipy.signal as sp
import numpy as np
from matplotlib import pyplot as plt

def fiducial_points(x,pks,fs,vis):
    """
    Description: Pulse detection and correction from pulsatile signals
    Inputs:  x, array with pulsatile signal [user defined units]
             pks, array with the position of the peaks [number of samples]
             fs, sampling rate of signal [Hz]
             vis, visualisation option [True, False]
    Outputs: fidp, dictionary with the positions of several fiducial points for the cardiac cycles [number of samples]

    Fiducial points:  1: Systolic peak (pks)
                      2: Onset, as the minimum before the systolic peak (ons)
                      3: Onset, using the tangent intersection method (ti)
                      4: Diastolic peak (dpk)
                      5: Maximum slope (m1d)
                      6: a point from second derivative PPG (a2d)
                      7: b point from second derivative PPG (b2d)
                      8: c point from second derivative PPG (c2d)
                      9: d point from second derivative PPG (d2d)
                      10: e point from second derivative PPG (e2d)
                      11: p1 from the third derivative PPG (p1)
                      12: p2 from the third derivative PPG (p2)

    Libraries: NumPy (as np), SciPy (Signal, as sp), Matplotlib (PyPlot, as plt)

    Version: 1.0 - June 2022

    Developed by: Elisa Mejía-Mejía
                   City, University of London

    Edited by: Peter Charlton (see "Added by PC")

    """
    # First, second and third derivatives
    d1x = sp.savgol_filter(x, 9, 5, deriv = 1)
    d2x = sp.savgol_filter(x, 9, 5, deriv = 2)
    d3x = sp.savgol_filter(x, 9, 5, deriv = 3)

    #plt.figure()
    #plt.plot(x/np.max(x))
    #plt.plot(d1x/np.max(d1x))
    #plt.plot(d2x/np.max(d2x))
    #plt.plot(d3x/np.max(d3x))

    # Search in time series: Onsets between consecutive peaks
    ons = np.empty(0)
    for i in range(len(pks) - 1):
        start = pks[i]
        stop = pks[i + 1]
        ibi = x[start:stop]
        #plt.figure()
        #plt.plot(ibi, color = 'black')
        aux_ons, = np.where(ibi == np.min(ibi))
        if len(aux_ons) > 1:
            aux_ons = aux_ons[0]
        ind_ons = aux_ons.astype(int)
        ons = np.append(ons, ind_ons + start)
        #plt.plot(ind_ons, ibi[ind_ons], marker = 'o', color = 'red')
    ons = ons.astype(int)
    #print('Onsets: ' + str(ons))
    #plt.figure()
    #plt.plot(x, color = 'black')
    #plt.scatter(pks, x[pks], marker = 'o', color = 'red')
    #plt.scatter(ons, x[ons], marker = 'o', color = 'blue')

    # Search in time series: Diastolic peak and dicrotic notch between consecutive onsets
    dia = np.empty(0)
    dic = np.empty(0)
    for i in range(len(ons) - 1):
        start = ons[i]
        stop = ons[i + 1]
        ind_pks, = np.intersect1d(np.where(pks < stop), np.where(pks > start))
        ind_pks = pks[ind_pks]
        ibi_portion = x[ind_pks:stop]
        ibi_2d_portion = d2x[ind_pks:stop]
        #plt.figure()
        #plt.plot(ibi_portion/np.max(ibi_portion))
        #plt.plot(ibi_2d_portion/np.max(ibi_2d_portion))
        aux_dic, _ = sp.find_peaks(ibi_2d_portion)
        aux_dic = aux_dic.astype(int)
        aux_dia, _ = sp.find_peaks(-ibi_2d_portion)
        aux_dia = aux_dia.astype(int)
        if len(aux_dic) != 0:
            ind_max, = np.where(ibi_2d_portion[aux_dic] == np.max(ibi_2d_portion[aux_dic]))
            aux_dic_max = aux_dic[ind_max]
            if len(aux_dia) != 0:
                nearest = aux_dia - aux_dic_max
                aux_dic = aux_dic_max
                dic = np.append(dic, (aux_dic + ind_pks).astype(int))
                #plt.scatter(aux_dic, ibi_portion[aux_dic]/np.max(ibi_portion), marker = 'o')
                ind_dia, = np.where(nearest > 0)
                aux_dia = aux_dia[ind_dia]
                nearest = nearest[ind_dia]
                if len(nearest) != 0:
                    ind_nearest, = np.where(nearest == np.min(nearest))
                    aux_dia = aux_dia[ind_nearest]
                    dia = np.append(dia, (aux_dia + ind_pks).astype(int))
                    #plt.scatter(aux_dia, ibi_portion[aux_dia]/np.max(ibi_portion), marker = 'o')
                    #break
            else:
                dic = np.append(dic, (aux_dic_max + ind_pks).astype(int))
                #plt.scatter(aux_dia, ibi_portion[aux_dia]/np.max(ibi_portion), marker = 'o')
    dia = dia.astype(int)
    dic = dic.astype(int)
    #plt.scatter(dia, x[dia], marker = 'o', color = 'orange')
    #plt.scatter(dic, x[dic], marker = 'o', color = 'green')

    # Search in D1: Maximum slope point
    m1d = np.empty(0)
    for i in range(len(ons) - 1):
        start = ons[i]
        stop = ons[i + 1]
        ind_pks, = np.intersect1d(np.where(pks < stop), np.where(pks > start))
        ind_pks = pks[ind_pks]
        ibi_portion = x[start:ind_pks]
        ibi_1d_portion = d1x[start:ind_pks]
        #plt.figure()
        #plt.plot(ibi_portion/np.max(ibi_portion))
        #plt.plot(ibi_1d_portion/np.max(ibi_1d_portion))
        aux_m1d, _ = sp.find_peaks(ibi_1d_portion)
        aux_m1d = aux_m1d.astype(int)
        if len(aux_m1d) != 0:
            ind_max, = np.where(ibi_1d_portion[aux_m1d] == np.max(ibi_1d_portion[aux_m1d]))
            aux_m1d_max = aux_m1d[ind_max]
            if len(aux_m1d_max) > 1:
                aux_m1d_max = aux_m1d_max[0]
            m1d = np.append(m1d, (aux_m1d_max + start).astype(int))
            #plt.scatter(aux_m1d, ibi_portion[aux_dic]/np.max(ibi_portion), marker = 'o')
            #break
    m1d = m1d.astype(int)
    #plt.scatter(m1d, x[m1d], marker = 'o', color = 'purple')

    # Search in time series: Tangent intersection points
    tip = np.empty(0)
    for i in range(len(ons) - 1):
        start = ons[i]
        stop = ons[i + 1]
        ibi_portion = x[start:stop]
        ibi_1d_portion = d1x[start:stop]
        ind_m1d, = np.intersect1d(np.where(m1d < stop), np.where(m1d > start))
        ind_m1d = m1d[ind_m1d] - start
        #plt.figure()
        #plt.plot(ibi_portion/np.max(ibi_portion))
        #plt.plot(ibi_1d_portion/np.max(ibi_1d_portion))
        #plt.scatter(ind_m1d, ibi_portion[ind_m1d]/np.max(ibi_portion), marker = 'o')
        #plt.scatter(ind_m1d, ibi_1d_portion[ind_m1d]/np.max(ibi_1d_portion), marker = 'o')
        aux_tip = np.round(((ibi_portion[0] - ibi_portion[ind_m1d])/ibi_1d_portion[ind_m1d]) + ind_m1d)
        aux_tip = aux_tip.astype(int)
        tip = np.append(tip, (aux_tip + start).astype(int))
        #plt.scatter(aux_tip, ibi_portion[aux_tip]/np.max(ibi_portion), marker = 'o')
        #break
    tip = tip.astype(int)
    #plt.scatter(tip, x[tip], marker = 'o', color = 'aqua')

    # Search in D2: A, B, C, D and E points
    a2d = np.empty(0)
    b2d = np.empty(0)
    c2d = np.empty(0)
    d2d = np.empty(0)
    e2d = np.empty(0)
    for i in range(len(ons) - 1):
        start = ons[i]
        stop = ons[i + 1]
        ibi_portion = x[start:stop]
        ibi_1d_portion = d1x[start:stop]
        ibi_2d_portion = d2x[start:stop]
        ind_m1d = np.intersect1d(np.where(m1d > start),np.where(m1d < stop))
        ind_m1d = m1d[ind_m1d]
        #plt.figure()
        #plt.plot(ibi_portion/np.max(ibi_portion))
        #plt.plot(ibi_1d_portion/np.max(ibi_1d_portion))
        #plt.plot(ibi_2d_portion/np.max(ibi_2d_portion))
        aux_m2d_pks, _ = sp.find_peaks(ibi_2d_portion)
        aux_m2d_ons, _ = sp.find_peaks(-ibi_2d_portion)
        # a point:
        ind_a, = np.where(ibi_2d_portion[aux_m2d_pks] == np.max(ibi_2d_portion[aux_m2d_pks]))
        ind_a = aux_m2d_pks[ind_a]
        if (ind_a < ind_m1d):
            a2d = np.append(a2d, ind_a + start)
            #plt.scatter(ind_a, ibi_2d_portion[ind_a]/np.max(ibi_2d_portion), marker = 'o')
            # b point:
            ind_b = np.where(ibi_2d_portion[aux_m2d_ons] == np.min(ibi_2d_portion[aux_m2d_ons]))
            ind_b = aux_m2d_ons[ind_b]
            if (ind_b > ind_a) and (ind_b < len(ibi_2d_portion)):
                b2d = np.append(b2d, ind_b + start)
                #plt.scatter(ind_b, ibi_2d_portion[ind_b]/np.max(ibi_2d_portion), marker = 'o')
        # e point:
        ind_e, = np.where(aux_m2d_pks > ind_m1d - start)
        aux_m2d_pks = aux_m2d_pks[ind_e]
        ind_e, = np.where(aux_m2d_pks < 0.6*len(ibi_2d_portion))
        ind_e = aux_m2d_pks[ind_e]
        if len(ind_e) >= 1:
            if len(ind_e) >= 2:
                ind_e = ind_e[1]
            e2d = np.append(e2d, ind_e + start)
            #plt.scatter(ind_e, ibi_2d_portion[ind_e]/np.max(ibi_2d_portion), marker = 'o')
            # c point:
            ind_c, = np.where(aux_m2d_pks < ind_e)
            if len(ind_c) != 0:
                ind_c_aux = aux_m2d_pks[ind_c]
                ind_c, = np.where(ibi_2d_portion[ind_c_aux] == np.max(ibi_2d_portion[ind_c_aux]))
                ind_c = ind_c_aux[ind_c]
                if len(ind_c) != 0:
                    c2d = np.append(c2d, ind_c + start)
                    #plt.scatter(ind_c, ibi_2d_portion[ind_c]/np.max(ibi_2d_portion), marker = 'o')
            else:
                aux_m1d_ons, _ = sp.find_peaks(-ibi_1d_portion)
                ind_c, = np.where(aux_m1d_ons < ind_e)
                ind_c_aux = aux_m1d_ons[ind_c]
                if len(ind_c) != 0:
                    ind_c, = np.where(ind_c_aux > ind_b)
                    ind_c = ind_c_aux[ind_c]
                    if len(ind_c) > 1:
                        ind_c = ind_c[0]
                    c2d = np.append(c2d, ind_c + start)
                    #plt.scatter(ind_c, ibi_2d_portion[ind_c]/np.max(ibi_2d_portion), marker = 'o')
            # d point:
            if len(ind_c) != 0:
                ind_d = np.intersect1d(np.where(aux_m2d_ons < ind_e), np.where(aux_m2d_ons > ind_c))
                if len(ind_d) != 0:
                    ind_d_aux = aux_m2d_ons[ind_d]
                    ind_d, = np.where(ibi_2d_portion[ind_d_aux] == np.min(ibi_2d_portion[ind_d_aux]))
                    ind_d = ind_d_aux[ind_d]
                    if len(ind_d) != 0:
                        d2d = np.append(d2d, ind_d + start)
                        #plt.scatter(ind_d, ibi_2d_portion[ind_d]/np.max(ibi_2d_portion), marker = 'o')
                else:
                    ind_d = ind_c
                    d2d = np.append(d2d, ind_d + start)
                    #plt.scatter(ind_d, ibi_2d_portion[ind_d]/np.max(ibi_2d_portion), marker = 'o')
    a2d = a2d.astype(int)
    b2d = b2d.astype(int)
    c2d = c2d.astype(int)
    d2d = d2d.astype(int)
    e2d = e2d.astype(int)
    #plt.figure()
    #plt.plot(d2x, color = 'black')
    #plt.scatter(a2d, d2x[a2d], marker = 'o', color = 'red')
    #plt.scatter(b2d, d2x[b2d], marker = 'o', color = 'blue')
    #plt.scatter(c2d, d2x[c2d], marker = 'o', color = 'green')
    #plt.scatter(d2d, d2x[d2d], marker = 'o', color = 'orange')
    #plt.scatter(e2d, d2x[e2d], marker = 'o', color = 'purple')

    # Search in D3: P1 and P2 points
    p1p = np.empty(0)
    p2p = np.empty(0)
    for i in range(len(ons) - 1):
        start = ons[i]
        stop = ons[i + 1]
        ibi_portion = x[start:stop]
        ibi_1d_portion = d1x[start:stop]
        ibi_2d_portion = d2x[start:stop]
        ibi_3d_portion = d3x[start:stop]
        ind_b = np.intersect1d(np.where(b2d > start),np.where(b2d < stop))
        ind_b = b2d[ind_b]
        ind_c = np.intersect1d(np.where(c2d > start),np.where(c2d < stop))
        ind_c = c2d[ind_c]
        ind_d = np.intersect1d(np.where(d2d > start),np.where(d2d < stop))
        ind_d = d2d[ind_d]
        ind_dic = np.intersect1d(np.where(dic > start),np.where(dic < stop))
        ind_dic = dic[ind_dic]
        #plt.figure()
        #plt.plot(ibi_portion/np.max(ibi_portion))
        #plt.plot(ibi_1d_portion/np.max(ibi_1d_portion))
        #plt.plot(ibi_2d_portion/np.max(ibi_2d_portion))
        #plt.plot(ibi_3d_portion/np.max(ibi_3d_portion))
        #plt.scatter(ind_b - start, ibi_3d_portion[ind_b - start]/np.max(ibi_3d_portion), marker = 'o')
        #plt.scatter(ind_c - start, ibi_3d_portion[ind_c - start]/np.max(ibi_3d_portion), marker = 'o')
        #plt.scatter(ind_d - start, ibi_3d_portion[ind_d - start]/np.max(ibi_3d_portion), marker = 'o')
        #plt.scatter(ind_dic - start, ibi_3d_portion[ind_dic - start]/np.max(ibi_3d_portion), marker = 'o')
        aux_p3d_pks, _ = sp.find_peaks(ibi_3d_portion)
        aux_p3d_ons, _ = sp.find_peaks(-ibi_3d_portion)
        # P1:
        if (len(aux_p3d_pks) != 0 and len(ind_b) != 0):
            ind_p1, = np.where(aux_p3d_pks > ind_b - start)
            if len(ind_p1) != 0:
                ind_p1 = aux_p3d_pks[ind_p1[0]]
                p1p = np.append(p1p, ind_p1 + start)
                #plt.scatter(ind_p1, ibi_3d_portion[ind_p1]/np.max(ibi_3d_portion), marker = 'o')
        # P2:
        if (len(aux_p3d_ons) != 0 and len(ind_c) != 0 and len(ind_d) != 0):
            if ind_c == ind_d:
                ind_p2, = np.where(aux_p3d_ons > ind_d - start)
                ind_p2 = aux_p3d_ons[ind_p2[0]]
            else:
                ind_p2, = np.where(aux_p3d_ons < ind_d - start)
                ind_p2 = aux_p3d_ons[ind_p2[-1]]
            if len(ind_dic) != 0:
                aux_x_pks, _ = sp.find_peaks(ibi_portion)
                if ind_p2 > ind_dic - start:
                    ind_between = np.intersect1d(np.where(aux_x_pks < ind_p2), np.where(aux_x_pks > ind_dic - start))
                else:
                    ind_between = np.intersect1d(np.where(aux_x_pks > ind_p2), np.where(aux_x_pks < ind_dic - start))
                if len(ind_between) != 0:
                    ind_p2 = aux_x_pks[ind_between[0]]
            p2p = np.append(p2p, ind_p2 + start)
            #plt.scatter(ind_p2, ibi_3d_portion[ind_p2]/np.max(ibi_3d_portion), marker = 'o')
    p1p = p1p.astype(int)
    p2p = p2p.astype(int)
    #plt.figure()
    #plt.plot(d3x, color = 'black')
    #plt.scatter(p1p, d3x[p1p], marker = 'o', color = 'green')
    #plt.scatter(p2p, d3x[p2p], marker = 'o', color = 'orange')

    # Added by PC: Magnitudes of second derivative points
    bmag2d = np.zeros(len(b2d))
    cmag2d = np.zeros(len(b2d))
    dmag2d = np.zeros(len(b2d))
    emag2d = np.zeros(len(b2d))
    for beat_no in range(0,len(b2d)):
        bmag2d[beat_no] = d2x[b2d[beat_no]]/d2x[a2d[beat_no]]
        cmag2d[beat_no] = d2x[c2d[beat_no]]/d2x[a2d[beat_no]]
        dmag2d[beat_no] = d2x[d2d[beat_no]]/d2x[a2d[beat_no]]
        emag2d[beat_no] = d2x[e2d[beat_no]]/d2x[a2d[beat_no]]

     # Added by PC: Refine the list of fiducial points to only include those corresponding to beats for which a full set of points is available
    off = ons[1:]
    ons = ons[:-1]
    if pks[0] < ons[0]:
        pks = pks[1:]
    if pks[-1] > off[-1]:
        pks = pks[:-1]

    # Visualise results
    if vis == True:
        fig, (ax1,ax2,ax3,ax4) = plt.subplots(4, 1, sharex = True, sharey = False, figsize=(10,10))
        fig.suptitle('Fiducial points')

        ax1.plot(x, color = 'black')
        ax1.scatter(pks, x[pks.astype(int)], color = 'orange', label = 'pks')
        ax1.scatter(ons, x[ons.astype(int)], color = 'green', label = 'ons')
        ax1.scatter(off, x[off.astype(int)], marker = '*', color = 'green', label = 'off')
        ax1.scatter(dia, x[dia.astype(int)], color = 'yellow', label = 'dia')
        ax1.scatter(dic, x[dic.astype(int)], color = 'blue', label = 'dic')
        ax1.scatter(tip, x[tip.astype(int)], color = 'purple', label = 'dic')
        ax1.legend()
        ax1.set_ylabel('x')

        ax2.plot(d1x, color = 'black')
        ax2.scatter(m1d, d1x[m1d.astype(int)], color = 'orange', label = 'm1d')
        ax2.legend()
        ax2.set_ylabel('d1x')

        ax3.plot(d2x, color = 'black')
        ax3.scatter(a2d, d2x[a2d.astype(int)], color = 'orange', label = 'a')
        ax3.scatter(b2d, d2x[b2d.astype(int)], color = 'green', label = 'b')
        ax3.scatter(c2d, d2x[c2d.astype(int)], color = 'yellow', label = 'c')
        ax3.scatter(d2d, d2x[d2d.astype(int)], color = 'blue', label = 'd')
        ax3.scatter(e2d, d2x[e2d.astype(int)], color = 'purple', label = 'e')
        ax3.legend()
        ax3.set_ylabel('d2x')

        ax4.plot(d3x, color = 'black')
        ax4.scatter(p1p, d3x[p1p.astype(int)], color = 'orange', label = 'p1')
        ax4.scatter(p2p, d3x[p2p.astype(int)], color = 'green', label = 'p2')
        ax4.legend()
        ax4.set_ylabel('d3x')

        plt.subplots_adjust(left = 0.1,
                            bottom = 0.1,
                            right = 0.9,
                            top = 0.9,
                            wspace = 0.4,
                            hspace = 0.4)

    # Creation of dictionary
    fidp = {'pks': pks.astype(int),
            'ons': ons.astype(int),
            'off': off.astype(int),  # Added by PC
            'tip': tip.astype(int),
            'dia': dia.astype(int),
            'dic': dic.astype(int),
            'm1d': m1d.astype(int),
            'a2d': a2d.astype(int),
            'b2d': b2d.astype(int),
            'c2d': c2d.astype(int),
            'd2d': d2d.astype(int),
            'e2d': e2d.astype(int),
            'bmag2d': bmag2d,
            'cmag2d': cmag2d,
            'dmag2d': dmag2d,
            'emag2d': emag2d,
            'p1p': p1p.astype(int),
            'p2p': p2p.astype(int)
            }

    return fidp
