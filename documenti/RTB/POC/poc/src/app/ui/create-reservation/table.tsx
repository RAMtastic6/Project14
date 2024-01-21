'use client';
import { getFilteredRestaurants } from '@/app/lib/data';
import { useSearchParams } from 'next/navigation';
import Link from 'next/link';


export default function RestaurantsTable() {
    const searchParams = useSearchParams();
    const nameRestaurant = searchParams.get('nameRestaurant');
    const date = searchParams.get('date');
    const city = searchParams.get('city');
    const cuisine = searchParams.get('cuisine');
    const parms = { date, nameRestaurant, city, cuisine };
    const restaurants = getFilteredRestaurants(parms);

    if (restaurants.length === 0) {
        return (
            <div>
                <p>Nessun ristorante trovato</p>
            </div>
        );
    }
    return (
        <div>
            <table className="min-w-full divide-y divide-gray-200 table-auto">
                <thead className="bg-gray-50">
                    <tr>
                        <th className="px-2 py-1 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Nome</th>
                        <th className="px-2 py-1 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Indirizzo</th>
                        <th className="px-2 py-1 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Città</th>
                        <th className="px-2 py-1 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Cucina</th>
                    </tr>
                </thead>
                <tbody className="bg-white divide-y divide-gray-200">
                    {restaurants.map((restaurant) => (
                        <tr key={restaurant.id}>
                            <td className="px-2 py-1 whitespace-nowrap"><Link href={`/create-reservation/${restaurant.id}/view`}>{restaurant.name}</Link></td>
                            <td className="px-2 py-1 whitespace-nowrap">{restaurant.address}</td>
                            <td className="px-2 py-1 whitespace-nowrap">{restaurant.city}</td>
                            <td className="px-2 py-1 whitespace-nowrap">{restaurant.cuisine}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}