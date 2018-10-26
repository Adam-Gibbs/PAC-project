Class MainWindow
    Public Temp As String = "One"

    Private Sub Button_Click_1(sender As Object, e As RoutedEventArgs)
        Dim DesignForm As Design_Window
        DesignForm = New Design_Window()
        DesignForm.Show()
        MsgBox(Temp)
    End Sub
End Class
