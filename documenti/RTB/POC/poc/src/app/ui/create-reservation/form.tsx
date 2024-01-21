
import { FormEvent, useState } from "react";
import { Restaurant } from "@/app/lib/definitions";
import ReservationModal from "@/app/ui/create-reservation/reservation-modal";

export default function Form({ restaurant }: { restaurant: Restaurant | null }) {
    const [isModalOpen, setModalOpen] = useState(false);
    const [formData, setFormData] = useState(new FormData());
    const [numberOfPeople, setNumberOfPeople] = useState(1);
    const [usernames, setUsernames] = useState<string[]>([]);
    const handleNumberOfPeopleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        const value = parseInt(event.target.value);
        setNumberOfPeople(value);
        setUsernames(Array(value).fill(""));
    };

    const handleUsernameChange = (index: number, event: React.ChangeEvent<HTMLInputElement>) => {
        const newUsername = event.target.value;
        setUsernames((prevUsernames) => {
            const updatedUsernames = [...prevUsernames];
            updatedUsernames[index] = newUsername;
            return updatedUsernames;
        });
    };
    const handleCloseModal = () => {
        setModalOpen(false);
    };
    const handleConfirm = (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        const formData = new FormData(e.target as HTMLFormElement);
        setFormData(formData);
        setModalOpen(true);
    };
    return (
        <>
            <form onSubmit={(e) => handleConfirm(e)}>
                <label>
                    Data:
                    <input name="date" type="date" />
                </label>
                <br />
                <label>
                    Ora di arrivo:
                    <input name="time" type="time" />
                </label>
                <br />
                <label>
                    Numero di persone:
                    <input name="numberOfPeople" type="number" value={numberOfPeople} onChange={handleNumberOfPeopleChange} />
                </label>
                <input name="restaurantId" type="hidden" value={restaurant?.id} />
                <br />
                {usernames.map((username, index) => (
                    <div key={index}>
                        <label>
                            Username {index + 1}:
                            <input name={`username${index}`} type="text" value={username} onChange={(event) => handleUsernameChange(index, event)} />
                        </label>
                        <br />
                    </div>
                ))}
                <button type="submit">Submit</button>
            </form>
            {isModalOpen && <ReservationModal isOpen={isModalOpen} onClose={handleCloseModal} formData={formData} />}
        </>
    );
}