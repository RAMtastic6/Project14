import React from 'react';
import Search from '@/app/ui/create-reservation/search';
import Table from '@/app/ui/create-reservation/table';

export default function Page() {
    return (
        <div className="container mx-auto">
            <div className="text-center">
                <h1 className="text-2xl font-bold">Prenota un tavolo</h1>
            </div>
            <div className="mt-4">
                <h2 className="text-lg font-bold">Ristoranti</h2>
                <p>Seleziona data, ora di arrivo, città e tipologia di cucina per ricercare un ristorante</p>
                <Search />
            </div>
            <Table />
        </div>
    );
};