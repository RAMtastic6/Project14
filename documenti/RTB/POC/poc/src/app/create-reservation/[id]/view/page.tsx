'use client';
import Form from '@/app/ui/create-reservation/form';
import { getRestaurantById } from '@/app/lib/data';

export default async function Page({ params }: { params: { id: string } }) {
    const id = params.id;
    const restaurant = getRestaurantById(id);
    return (
        <main>
            <h1 className="text-3xl font-bold">{restaurant?.name}</h1>
            <p>Indirizzo: {restaurant?.address}</p>
            <p>Città: {restaurant?.city}</p>
            <p>Cucina: {restaurant?.cuisine}</p>
            <h2 className="reservation-title text-2xl font-bold">Effettua una prenotazione</h2>
            <Form restaurant={restaurant} />
        </main>
    );
}