package src.test.java.org.ejemplo;
import static org.junit.Assert.assertEquals;
import org.junit.Test;

import src.main.java.org.ejemplo.Calculadora;

public class CalculadoraTest {

    @Test
    public void testSuma() {
        Calculadora calc = new Calculadora();
        assertEquals(5, calc.suma(2, 3));
    }

    @Test
    public void testResta() {
        Calculadora calc = new Calculadora();
        assertEquals(1, calc.resta(3, 2));
    }
}
