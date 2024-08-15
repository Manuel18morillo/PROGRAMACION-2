/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.vehiculos_manuel;

/**
 *
 * @author Moril
 */
public class Vehiculos_Manuel {

    public static void main(String[] args) {
        
        Vehiculo v = new Vehiculo();
        v.setMarca("Toyota");
        System.out.println(v.getMarca());
        
        v.setFabricante("Toyota motor corporation");
        System.out.println(v.getFabricante());
        
        v.setModelo("Fortuner");
        System.out.println(v.getModelo());
        
        v.setAño(2005);
        System.out.println(v.getAño());
        
        
        
        
    }
}
