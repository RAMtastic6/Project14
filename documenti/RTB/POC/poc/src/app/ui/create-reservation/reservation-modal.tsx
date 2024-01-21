import React from 'react';
import Modal from 'react-modal';
import { createReservation } from '@/app/lib/actions';
import Link from 'next/link';

export default function ReservationModal({ isOpen, onClose, formData }: { isOpen: boolean, onClose: () => void,formData:FormData }): JSX.Element {

    return (
        <Modal isOpen={isOpen} onRequestClose={onClose}>
            <h2>Riepilogo Prenotazione</h2>
            <p>Data: {String(formData.get("date"))}</p>
            <p>Ora: {String(formData.get("time"))}</p>
            <p>Numero di persone: {formData.get("numberOfPeople")?.toString()}</p>
            
            <Link href="/create-reservation">
                <button onClick={() => createReservation(formData)}>Conferma</button>
            </Link>
            <button onClick={onClose}>Annulla</button>
        </Modal>
    );
};
