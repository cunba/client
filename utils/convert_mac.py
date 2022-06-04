
class ConvertMac():
    def mac_to_string(self, mac):
        macList = mac.split(':')
        newMac = ''
        for i in range(0, len(macList)):
            newMac = newMac + macList[i]
        return newMac

    def string_to_mac(self, mac):
        string = ''
        for i in range(0, len(mac)):
            if i % 2 == 0 or i == len(mac)-1:
                string = string + mac[i]
            else:
                string = string + mac[i] + ':'
        return string