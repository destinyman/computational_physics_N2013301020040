temp=['      *       ',
      '     * *      ',
'    *****     ',
'   *     *    ',
'  *       *   ',
'    ******    ',
'    *     *   ',
'    ******    ',
'    *     *   ',
'    ******    ',
'    ******    ',
'   *          ',
'   *          ',
'   *          ',
'    ******    ',
'   ******     ',
'   *     *    ',
'   *     *    ',
'   *     *    ',
'   ******     ',
'   *******    ',
'   *          ',
'   *******    ',
'   *          ',
'   *******    ',
'   *******    ',
'   *          ',
'   ******     ',
'   *          ',
'   *          ',
'    ******    ',
'   *          ',
'   *  ****    ',
'   *     *    ',
'    ******    ',
'   *     *    ',
'   *     *    ',
'   *******    ',
'   *     *    ',
'   *     *    ',
'    *****     ',
'      *       ',
'      *       ',
'      *       ',
'    *****     ',
'     ***      ',
'      *       ',
'      *       ',
'  *   *       ',
'   ***        ',
'   *    *     ',
'   *  *       ',
'   **         ',
'   *  *       ',
'   *    *     ',
'   *          ',
'   *          ',
'   *          ',
'   *          ',
'   ******     ',
'   *     *    ',
'   **   **    ',
'   *  *  *    ',
'   *     *    ',
'   *     *    ',
'   *    *     ',
'   **   *     ',
'   * *  *     ',
'   *  * *     ',
'   *    *     ',
'    *****     ',
'   *     *    ',
'   *     *    ',
'   *     *    ',
'    *****     ',
'    *****     ',
'   *     *    ',
'   * * *      ',
'   *          ',
'   *          ',
'    *****     ',
'   *     *    ',
'   *  ** *    ',
'   *     *    ',
'    ***** **  ',
'   ******     ',
'   *     *    ',
'   ******     ',
'   *  *       ',
'   *    **    ',
'    *****     ',
'   *          ',
'     *        ',
'        *     ',
'   *****      ',
'   *******    ',
'      *       ',
'      *       ',
'      *       ',
'      *       ',
'   *      *   ',
'   *      *   ',
'   *      *   ',
'   *      *   ',
'    ******    ',
'  *     *     ',
'  *     *     ',
'   *   *      ',
'    * *       ',
'     *        ',
'  *       *   ',
'  *       *   ',
'  *   *   *   ',
'  * *   * *   ',
'  *       *   ',
'   **   **    ',
'     * *      ',
'      *       ',
'     * *      ',
'   **   **    ',
'   **    **   ',
'     *  *     ',
'      *       ',
'      *       ',
'      *       ',
'   *******    ',
'        *     ',
'      *       ',
'    *         ',
'   *******    '] 

name = raw_input("your name:")
N = len(name)

b=['$    ']
m1=b[0]
m2=b[0]
m3=b[0]
m4=b[0]
m5=b[0]

i = 0
while (i<N):
        cha = name[i]
        n = ord(cha)
        n1 = 5*(n-97)
        n2 = 5*(n-97) + 1
        n3 = 5*(n-97) + 2
        n4 = 5*(n-97) + 3
        n5 = 5*(n-97) + 4
        m1 = m1 + temp[n1]
        m2 = m2 + temp[n2]
        m3 = m3 + temp[n3]
        m4 = m4 + temp[n4]
        m5 = m5 + temp[n5]
        i = i + 1

print m1
print m2
print m3
print m4
print m5
