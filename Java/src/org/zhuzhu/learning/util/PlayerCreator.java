package org.zhuzhu.learning.util;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Random;

import org.zhuzhu.learning.model.Defender;
import org.zhuzhu.learning.model.Forward;
import org.zhuzhu.learning.model.Goalkeeper;
import org.zhuzhu.learning.model.Midfielder;
import org.zhuzhu.learning.model.Player;

/**
 * 
 * @author Chenfeng Zhu
 *
 */
public class PlayerCreator {

    protected static final List<Class<? extends Player>> allTypes = Collections
            .unmodifiableList(Arrays.asList(Goalkeeper.class, Defender.class, Midfielder.class, Forward.class));

    private static Random rand = new Random();

    public static Player generateRandomPlayer() {
        int n = rand.nextInt(allTypes.size());
        try {
            return allTypes.get(n).newInstance();
        } catch (InstantiationException e) {
            throw new RuntimeException(e);
        } catch (IllegalAccessException e) {
            throw new RuntimeException(e);
        }
    }

    public static ArrayList<Player> generateArrayList(int size) {
        ArrayList<Player> players = new ArrayList<>(size);
        for (int i = 0; i < size; i++) {
            players.add(generateRandomPlayer());
        }
        return players;
    }

}
