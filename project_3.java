/**
 * Animal class. Uses Eat method so the animal can eat.
 * @author JavatPoint
 * @since Week 3 of CSC6301
 * @see https://www.javatpoint.com/inheritance-in-java
 * @version 1.0
 */

class Animal {
    void eat() {
        System.out.println("eating...");
    }  
}  

/**
 * Dog class extends Animal class. It can eat and bark. 
 * 
 * @author JavatPoint
 * @since Week 3 of CSC6301
 * @see https://www.javatpoint.com/inheritance-in-java
 * @version 1.0
 */
class Dog extends Animal {  
    void bark() {
        System.out.println("barking...");
    }  
}  

/**
 * BabyDog Class extends Dog which extends Animal. It can eat, bark, and weep.
 * 
 * @author JavatPoint 
 * @since Week 3 of CSC6301
 * @see https://www.javatpoint.com/inheritance-in-java
 * @version 1.0
 */
class BabyDog extends Dog {  
    void weep() { 
        System.out.println("weeping...");
    }  
}  

/**
 * Cat Class extends Animal. Does not extend Dog. It can eat, meow, and hiss.
 * But cannot bark or weep.
 * 
 * @author Anthony Masse
 * @since Week 3 of CSC6301
 * @version 1.0
 */
class Cat extends Animal {
    void meow(){
        System.out.println("meowing...");
    }
    void hiss(){
        System.out.println("hissing...");
    }
}


class TestInheritance2 {  
    /**
     * @author Anthony Masse and JavatPoint 
     * @param args default paramter for a main - not used
     * @see https://www.javatpoint.com/inheritance-in-java
     * @since Week 3 of CSC6301
     */
    public static void main(String args[]){  
        BabyDog d = new BabyDog();
        System.out.println("The Baby Dog is:");  
        d.weep();  
        d.bark();  
        d.eat();

        //edited to use more than one class, added to use Cat class and methods
        Cat c = new Cat();
        System.out.println("But the Cat is:");
        c.hiss();
        c.eat();
        c.meow();

    }
}  