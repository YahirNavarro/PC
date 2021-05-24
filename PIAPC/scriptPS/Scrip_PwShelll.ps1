

$PFRed = Get-NetConnectionProfile
$opc = $args[0]

Switch ($opc){
    "Status" {
        $Res = "El perfil del firewall se encuentra en modo " + $PFRed.NetworkCategory
    }
    "Public" {
        if($PFRed.NetworkCategory -eq "Public"){
            $Res = "El perfil del firewall ya estaba en modo Publico."
        } else{
            Set-NetConnectionProfile -Name $PFRed.Name -NetworkCategory Public
            $Res = "Perfil cambiado de Privado a Publico."
        }
    }
    "Private" {
        if($PFRed.NetworkCategory -eq "Private"){
            $Res = "El perfil del firewall ya estaba en modo Privado."
        } else{
            Set-NetConnectionProfile -Name $PFRed.Name -NetworkCategory Private
            $Res = "Perfil cambiado de Publico a Privado."
        }
    }
    default {$Res = "ERROR. Ingrese una opcion valida."}
}

Write-Host $Res