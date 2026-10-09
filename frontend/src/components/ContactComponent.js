import './ContactsComponent.css';

const ContactComponent = ({contact}) => {
    return (
        <div className="contact-card">
            <p>ID: {contact.id}</p>
            <p>Name: {contact.name}</p>
            <p>Email: {contact.email}</p>
            <p>Phone: {contact.phone}</p>
            <p>Company: {contact.company}</p>
            <p>Status: {contact.status}</p>
        </div>
    );
};

export {
    ContactComponent
}