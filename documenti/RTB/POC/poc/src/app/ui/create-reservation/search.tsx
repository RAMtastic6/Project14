'use client';
import React, { useState } from 'react';
import { getCities, getCuisines } from '@/app/lib/data';
import { useSearchParams, usePathname, useRouter } from 'next/navigation';
import { useDebouncedCallback } from 'use-debounce';

export default function Search() {
    const searchParams = useSearchParams();
    const pathname = usePathname();
    const { replace } = useRouter();
    const handleSearch = useDebouncedCallback((nameRestaurant: string, date: string, city: string, cuisine: string) => {
        console.log('searching...', nameRestaurant, date, city, cuisine);
        const params = new URLSearchParams(searchParams);
        if (date) {
            params.set('date', date);
        } else {
            params.delete('date');
        }
        if (nameRestaurant) {
            params.set('nameRestaurant', nameRestaurant);
        }
        else {
            params.delete('nameRestaurant');
        }
        if (city) {
            params.set('city', city);
        } else {
            params.delete('city');
        }
        if (cuisine) {
            params.set('cuisine', cuisine);
        } else {
            params.delete('cuisine');
        }
        replace(`${pathname}?${params.toString()}`);
    }, 300);
    const [date, setDate] = useState('');
    const [nameRestaurant, setNameRestaurant] = useState('');
    const [city, setCity] = useState('');
    const [cuisine, setCuisine] = useState('');

    const cuisines = getCuisines();
    const cities = getCities();

    return (
        <div className="mb-4">
            <form onSubmit={(e) => e.preventDefault()} className="flex flex-col">
                <input
                    type="text"
                    value={nameRestaurant}
                    className="peer block w-full rounded-md border border-gray-200 py-[9px] pl-10 text-sm outline-2 placeholder:text-gray-500"
                    placeholder={'Nome ristorante'}
                    onChange={(e) => {
                        setNameRestaurant(e.target.value);
                        handleSearch(e.target.value, date, city, cuisine);
                    }}
                />
                <input
                    type="date"
                    value={date}
                    onChange={(e) => {
                        setDate(e.target.value);
                        handleSearch(nameRestaurant, e.target.value, city, cuisine);
                    }}
                    className="border border-gray-300 p-2 w-full mb-2"
                    min={new Date().toISOString().split('T')[0]} 
                />
                <input
                    type="text"
                    value={city}
                    onChange={(e) => {
                        setCity(e.target.value);
                        handleSearch(nameRestaurant, date, e.target.value, cuisine);
                    }}
                    placeholder="Città"
                    className="border border-gray-300 p-2 w-full mb-2"
                    list="citySuggestions"
                />
                <datalist id="citySuggestions">
                    {cities.map((city) => (
                        <option key={city} value={city} />
                    ))}
                </datalist>
                <select
                    value={cuisine}
                    onChange={(e) => {
                        setCuisine(e.target.value);
                        handleSearch(nameRestaurant, date, city, e.target.value);
                    }}
                    className="border border-gray-300 p-2 w-full mb-2"
                >
                    <option value="">Seleziona la tipologia di cucina</option>
                    {cuisines.map((cuisine) => (
                        <option key={cuisine} value={cuisine}>{cuisine}</option>
                    ))}
                </select>
                <button
                    onClick={() => {
                        setNameRestaurant('');
                        setDate('');
                        setCity('');
                        setCuisine('');
                        handleSearch('', '', '', '');
                    }}
                    className="bg-blue-500 text-white py-2 px-4 rounded-md"
                >
                    Reset
                </button>
            </form>
        </div>
    );
}