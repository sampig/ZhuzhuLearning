package org.zhuzhu.learning.containers;

import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.TreeMap;

/**
 * Compare HashMap, LinkedHashMap and TreeMap.
 * 
 * @author Chenfeng Zhu
 *
 */
public class MapSimpleTest {

    private int[] integers = { 1, -2, 0, 3, -4 };

    public void testHashMap() {
        HashMap<Integer, String> map = new HashMap<Integer, String>();
        for (int i : integers) {
            map.put(i, Integer.toString(i));
        }
        System.out.print("HashMap oder: ");
        System.out.println(map);
        for (int k : map.keySet()) {
            System.out.print(k + ", ");
        }
        System.out.println("\n");
    }

    public void testLinkedHashMap() {
        LinkedHashMap<Integer, String> map = new LinkedHashMap<Integer, String>(0, 0.75f, true);
        for (int i : integers) {
            map.put(i, Integer.toString(i));
        }
        System.out.print("LinkedHashMap oder: ");
        System.out.println(map);
        for (int k : map.keySet()) {
            System.out.print(k + ", ");
        }
        System.out.println();
        map.get(integers[2]);
        System.out.print("LinkedHashMap oder after accessing: ");
        System.out.println(map);
        System.out.println();
    }

    public void testTreeMap() {
        TreeMap<Integer, String> map = new TreeMap<Integer, String>();
        for (int i : integers) {
            map.put(i, Integer.toString(i));
        }
        System.out.print("TreeMap oder: ");
        System.out.println(map);
        for (int k : map.keySet()) {
            System.out.print(k + ", ");
        }
        System.out.println("\n");
    }

    public static void main(String... strings) {
        MapSimpleTest st = new MapSimpleTest();
        st.testHashMap();
        st.testLinkedHashMap();
        st.testTreeMap();
    }

}
