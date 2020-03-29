package tinysat.base;

public class Variable{
    private int id;
    private Boolean value;

    public Variable(int id) {
        this.id = id;
        this.value = null; // The value is unassigned
    }

    public Variable(int id, boolean value) {
        this.id = id;
        this.value = value;
    }

    public static Variable litToVar(int literal) {
        int id = literal / 2;
        boolean value = literal % 2 == 0;
        return new Variable(id, value);
    }

    public Variable clone() {
        return new Variable(this.id, this.value);
    }

    public void assign(boolean value) {
        this.value = value;
    }

    public void unassign() {
        this.value = null;
    }

    public boolean assigned() {
        return this.value != null;
    }

    public int toLit() {
        return (id - 1) * 2 + (value ? 1 : 0);
    }

    public int getId() {
        return id;
    }

    public Boolean getValue() {
        return value;
    }
}
