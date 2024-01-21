'use server';
import {reservations} from '@/app/lib/dati-di-prova';

export async function createReservation(formData: FormData) {
    const rawFormData: {
        restaurantId: string | null;
        date: string | null;
        time: string | null;
        numberOfPeople: number;
        usernames: string[];
    } = {
        restaurantId: formData.get('restaurantId')?.toString() || null,
        date: formData.get('date')?.toString() || null,
        time: formData.get('time')?.toString() || null,
        numberOfPeople: Number(formData.get('numberOfPeople')) || 0,
        usernames: [] as string[],
    };

    for (let i = 0; i < rawFormData.numberOfPeople; i++) {
        const username = formData.get(`username${i}`) as string;
        rawFormData.usernames.push(username);
    }

    reservations.push({
        id: reservations.length + 1,
        date: rawFormData.date!,
        time: rawFormData.time!,
        numberOfPeople: rawFormData.numberOfPeople,
        restaurantId: Number(rawFormData.restaurantId!),
        customers: rawFormData.usernames,
    });
    console.log(reservations);
}