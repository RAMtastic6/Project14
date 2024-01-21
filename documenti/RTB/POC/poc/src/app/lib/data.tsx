import {
    Restaurant,
    Menu,
    Food,
    Order
} from "@/app/lib/definitions";
import { getDayOfWeek } from '@/app/lib/utils';

export default function getRestaurants(): Restaurant[] {
    return [
        {
            id: 1,
            name: "Ristorante 1",
            address: "Via Roma",
            city: "Roma",
            cuisine: "Italiana",
            daysopen: ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì"],
            hours: "12:00 - 15:00, 19:00 - 23:00",
            menu: {
                id: 1,
                name: "Menu 1",
                items: [
                    {
                        id: 1,
                        name: "Spaghetti alla carbonara",
                        price: 10
                    },
                    {
                        id: 2,
                        name: "Spaghetti all'amatriciana",
                        price: 9
                    },
                    {
                        id: 3,
                        name: "Spaghetti al pomodoro",
                        price: 8
                    }
                ]
            }
        },
        {
            id: 2,
            name: "Ristorante 2",
            address: "Via Milano",
            city: "Milano",
            cuisine: "Cinese",
            daysopen: ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato"],
            hours: "12:00 - 15:00, 19:00 - 23:00",
            menu: {
                id: 2,
                name: "Menu 2",
                items: [
                    {
                        id: 4,
                        name: "Riso alla cantonese",
                        price: 10
                    },
                    {
                        id: 5,
                        name: "Riso fritto",
                        price: 9
                    },
                    {
                        id: 6,
                        name: "Riso saltato",
                        price: 8
                    }
                ]
            }
        },
        {
            id: 3,
            name: "Ristorante 3",
            address: "Via Napoli",
            city: "Napoli",
            cuisine: "Pizza",
            daysopen: ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"],
            hours: "12:00 - 15:00, 19:00 - 23:00",
            menu: {
                id: 3,
                name: "Menu 3",
                items: [
                    {
                        id: 7,
                        name: "Pizza margherita",
                        price: 10
                    },
                    {
                        id: 8,
                        name: "Pizza marinara",
                        price: 9
                    },
                    {
                        id: 9,
                        name: "Pizza capricciosa",
                        price: 8
                    }
                ]
            }
        }
    ];
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