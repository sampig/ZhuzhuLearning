package org.zhuzhu.learning.model;

public class Player implements Comparable<Player> {

    private String name;

    public Player() {
        this.name = "pname";
    }

    public Player(String name) {
        this.name = name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return this.getClass().getSimpleName() + "-" + this.name;
    }

    @Override
    public int compareTo(Player o) {
        return this.getClass().getSimpleName().compareTo(o.getClass().getSimpleName());
    }

}
