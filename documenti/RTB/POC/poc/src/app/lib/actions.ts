'use server';

export async function createReservation(formData: FormData){;
    const rawFormData = {
        restaurantId: formData.get('restaurantId'),
        date: formData.get('date'),
        time: formData.get('time'),
        numberOfPeople: formData.get('numberOfPeople'),
    };
    console.log(rawFormData);
}