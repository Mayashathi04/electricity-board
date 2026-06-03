document.addEventListener('DOMContentLoaded', () => {
    const connectionForm = document.getElementById('connection-form');
    const connectionsGrid = document.getElementById('connections-grid');

    fetchConnections();

    connectionForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const consumer_name = document.getElementById('consumer-name').value;
        const connection_type = document.getElementById('connection-type').value;
        const sanctioned_load = document.getElementById('sanctioned-load').value;

        const response = await fetch('/api/connections', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ consumer_name, connection_type, sanctioned_load })
        });

        if (response.ok) {
            connectionForm.reset();
            fetchConnections();
        }
    });

    async function fetchConnections() {
        const response = await fetch('/api/connections');
        const connections = await response.json();
        
        connectionsGrid.innerHTML = '';
        
        if (connections.length === 0) {
            connectionsGrid.innerHTML = `<p style="color: #64748b; grid-column: 1/-1; text-align: center; padding: 25px;">No registered electricity power grid loops recorded.</p>`;
            return;
        }

        connections.forEach(line => {
            const card = document.createElement('div');
            card.className = 'project-card';
            const isSuspended = line.status === 'Suspended';
            
            card.innerHTML = `
                <div class="card-header">
                    <h3 style="${isSuspended ? 'text-decoration: line-through; color: #475569;' : ''}">${line.consumer_name}</h3>
                    <span class="meta-tag"><i class="fa-solid fa-building-user"></i> ${line.connection_type}</span>
                    <p><i class="fa-solid fa-gauge-high"></i> Allocated Power: <strong>${line.sanctioned_load} kW</strong></p>
                </div>
                <div class="card-actions">
                    <span class="status-badge ${line.status.toLowerCase()}" onclick="toggleGridLine(${line.id}, '${line.status}')">
                        ${line.status}
                    </span>
                    <button class="btn-delete" onclick="terminateLine(${line.id})">
                        <i class="fa-regular fa-trash-can"></i>
                    </button>
                </div>
            `;
            connectionsGrid.appendChild(card);
        });
    }

    window.toggleGridLine = async (id, currentStatus) => {
        const nextStatus = currentStatus === 'Active' ? 'Suspended' : 'Active';
        await fetch(`/api/connections/${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ status: nextStatus })
        });
        fetchConnections();
    };

    window.terminateLine = async (id) => {
        if(confirm("Permanently cut transmission line metrics and erase data structure record entry?")) {
            await fetch(`/api/connections/${id}`, { method: 'DELETE' });
            fetchConnections();
        }
    };
});