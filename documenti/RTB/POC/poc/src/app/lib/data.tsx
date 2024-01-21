import {
    Restaurant,
    Menu,
    Food,
    Order,
    Reservation,
} from "@/app/lib/definitions";
import { restaurants, reservations } from "@/app/lib/dati-di-prova";
import { getDayOfWeek } from '@/app/lib/utils';

export default function getRestaurants(): Restaurant[] {
    return restaurants;
}

export function getReservations(): Reservation[] {
    return reservations;
}

export function getReservationById(id: number): Reservation | null {
    const reservations = getReservations();
    return reservations.find((reservation) => reservation.id === id) || null;
}

export function getMenuByRestaurantId(id: number): Menu | null {
    const restaurants = getRestaurants();
    const restaurant = restaurants.find((restaurant) => restaurant.id === id);
    return restaurant ? restaurant.menu : null;
}

export function getCuisines(): string[] {
    const restaurants = getRestaurants();
    return Array.from(new Set(restaurants.map((restaurant) => restaurant.cuisine)));
}

export function getCities(): string[] {
    const restaurants = getRestaurants();
    return Array.from(new Set(restaurants.map((restaurant) => restaurant.city)));
}

export function getFilteredRestaurants(query: { date: string | null; nameRestaurant: string | null; city: string | null; cuisine: string | null; }): Restaurant[] {
    const restaurants = getRestaurants();
    return restaurants.filter((restaurant) => {
        if (query.date) {
            const dayOfWeek = getDayOfWeek(new Date(query.date));
            if (!restaurant.daysopen.includes(dayOfWeek)) {
                return false;
            }
        }
        if(query.nameRestaurant && !restaurant.name.includes(query.nameRestaurant)) {
            return false;
        }
        if (query.city && restaurant.city !== query.city) {
            return false;
        }
        if (query.cuisine && restaurant.cuisine !== query.cuisine) {
            return false;
        }
        return true;
    });
}

export function getRestaurantById(id: string): Restaurant | null {
    const restaurants = getRestaurants();
    return restaurants.find((restaurant) => restaurant.id.toString() === id) || null;
}