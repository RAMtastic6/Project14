import {
    Restaurant,
    Menu,
    Food,
    Order,
    Reservation,
} from "@/app/lib/definitions";


export const restaurants: Restaurant[] = [
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

export const reservations: Reservation[] = [
    {
        id: 1,
        date: "2021-06-01",
        time: "12:00",
        numberOfPeople: 2,
        restaurantId: 1,
        customers: ["Mario Rossi", "Luigi Bianchi"]
    },
    {
        id: 2,
        date: "2021-06-02",
        time: "12:00",
        numberOfPeople: 2,
        restaurantId: 2,
        customers: ["Mario Rossi", "Luigi Bianchi"]
    },
    {
        id: 3,
        date: "2021-06-03",
        time: "12:00",
        numberOfPeople: 2,
        restaurantId: 3,
        customers: ["Mario Rossi", "Luigi Bianchi"]
    }
];