function toggleSNMPv3Fields() {
    // Récupérer le formulaire
    var form = document.getElementById("addEquipementForm");

    // Récupérer la case à cocher
    var snmpv3Checkbox = document.getElementById("snmpv3");

    // Récupérer le champ de formulaire conditionnel
    var snmpv3Fields = document.getElementById("snmpv3Fields");
    var snmpv2Fields = document.getElementById("snmpv2Fields");
    var portInput = document.getElementById("portInput");
    var communauteInput = document.getElementById("communauteInput");

    // Ajouter un écouteur d'événements pour détecter les changements dans la case à cocher
    snmpv3Checkbox.addEventListener("change", function() {
        // Si la case à cocher est cochée, rendre le champ de formulaire SNMPv2 facultatif
        // Sinon, rendre le champ de formulaire SNMPv2 obligatoire
        portInput.required = !snmpv3Checkbox.checked;
        communauteInput.required = !snmpv3Checkbox.checked;

        // Mettre à jour l'action en fonction de l'état de la case à cocher
        if (snmpv3Checkbox.checked) {
            snmpv3Fields.style.display = "block";
            snmpv2Fields.style.display = "none";
            form.action = "/add_equipmentv3";
        } else {
            snmpv3Fields.style.display = "none";
            snmpv2Fields.style.display = "block";
            form.action = "/add_equipment";
        }
    });
}