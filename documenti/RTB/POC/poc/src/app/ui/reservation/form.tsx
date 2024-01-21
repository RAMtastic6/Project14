import { createReservation } from "@/app/lib/actions";
import { Restaurant } from "@/app/lib/definitions";

export default function Form({ restaurant }: { restaurant: Restaurant | null }) {
    return (
        <form action={createReservation}>
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
                <input name="numberOfPeople" type="number" />
            </label>
            <input name="restaurantId" type="hidden" value={restaurant?.id} />
            <br />
            <button type="submit">Submit</button>
        </form>
    );
}