import {useForm} from "react-hook-form";
import {createUpdateDeleteContacts} from "../services/service";
import './ContactForm.css';

const ContactForm = ({onCreated}) => {
    const {register, handleSubmit, reset, setError, formState: {errors}} = useForm();
    const saveContact = async (contact) => {
        try {
            const created = await createUpdateDeleteContacts.createContact(contact);
            reset();
            if (onCreated) {
                onCreated(created)
            }
        } catch (error) {
            console.error(error.response?.data)

            const serverErrors = error.response?.data;
            if (error.response?.status === 400 && serverErrors) {
                Object.entries(serverErrors).forEach(([field, messages]) => {
                    setError(field, {type: 'server', message: messages[0]});
                })
            }

        }

    }
    return (
        <form className="contact-form" onSubmit={handleSubmit(saveContact)}>
            <input type="text" placeholder={'name'} required {...register('name')}/>
            <input type="email" placeholder={'email'} required {...register('email')}/>
            {errors.email && <span className="error">{errors.email.message}</span>}
            <input type="text" placeholder={'+380 XX-XXX-XXXX'} required {...register('phone')}/>
            <input type="text" placeholder={'company'} required {...register('company')}/>
            <select {...register('status')}>
                <option value="New">New</option>
                <option value="Contacted">Contacted</option>
                <option value="Customer">Customer</option>
            </select>
            <button type={'submit'}>add</button>
        </form>
    );
};

export default ContactForm;