package org.zhuzhu.learning.containers;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Random;

import org.zhuzhu.learning.model.Defender;
import org.zhuzhu.learning.model.Forward;
import org.zhuzhu.learning.model.Goalkeeper;
import org.zhuzhu.learning.model.Player;
import org.zhuzhu.learning.util.PlayerCreator;

/**
 * 
 * @author Chenfeng Zhu
 *
 */
public class ListSimpleTest {

    public static void main(String[] strings) {
        Random rand = new Random();

        List<Player> players = PlayerCreator.generateArrayList(5);
        System.out.println("01 players: " + players);

        Defender d = new Defender("Barzagli");
        players.add(d);
        System.out.println("02 players: " + players);
        System.out.println("03 players.contains: " + players.contains(d));
        players.remove(d);
        System.out.println("04 players: " + players);

        Player p2 = players.get(2);
        System.out.println("05 p2:" + p2 + " in " + players.indexOf(p2));

        Player g = new Goalkeeper();
        System.out.println("06 players.indexOf: " + players.indexOf(g));
        System.out.println("07 players.remove: " + players.remove(g));

        System.out.println("08 players: " + players);
        players.add(3, new Forward());
        System.out.println("09 players: " + players);

        List<Player> sub = players.subList(1, 3);
        System.out.println("10 subList: " + sub);
        System.out.println("11 containsAll: " + players.containsAll(sub));
        Collections.sort(sub);
        System.out.println("12 sorted sub: " + sub);
        System.out.println("13 containsAll: " + players.containsAll(sub));
        Collections.shuffle(sub, rand);
        System.out.println("14 shuffle: " + sub);
        System.out.println("15 containsAll: " + players.containsAll(sub));

        List<Player> copy = new ArrayList<Player>(players);
        System.out.println("16 copy: " + copy);
        sub = Arrays.asList(players.get(1), players.get(3));
        System.out.println("17 sub: " + sub);
        copy.retainAll(sub);
        System.out.println("18 copy: " + copy);
        copy = new ArrayList<Player>(players);
        System.out.println("19 copy: " + copy);
        copy.remove(2);
        System.out.println("20 copy: " + copy);
        copy.set(1, new Defender("Chiellini"));
        System.out.println("21 copy: " + copy);
        copy.addAll(2, sub);
        System.out.println("22 copy: " + copy);

        System.out.println("23 players: " + players);
        System.out.println("24 players.isEmpty: " + players.isEmpty());
        players.clear();
        System.out.println("25 players: " + players);
        System.out.println("26 players.isEmpty: " + players.isEmpty());
    }

}
