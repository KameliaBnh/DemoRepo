package GUI;

import java.awt.FileDialog;

/**
 *
 * @author Kamelia Benhamna
 */
public class MainFrame extends javax.swing.JFrame {

    String filename = null;
    
    /**
     * Creates new form MainFrame
     */
    public MainFrame() {
        initComponents();
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        visualisationPane2 = new GUI.VisualisationPane();
        optionsPane1 = new GUI.OptionsPane();
        Yolov5_button = new javax.swing.JRadioButton();
        Yolov8_button = new javax.swing.JRadioButton();
        ModelChoice = new javax.swing.JLabel();
        TrackingVideo = new javax.swing.JCheckBox();
        Start = new javax.swing.JButton();
        statisticsPane1 = new GUI.StatisticsPane();
        SpeciesName = new javax.swing.JLabel();
        SpeciesInfo = new javax.swing.JLabel();
        MenuBar = new javax.swing.JMenuBar();
        Open = new javax.swing.JMenu();
        OpenFile = new javax.swing.JMenuItem();
        Export = new javax.swing.JMenu();
        ExportHTML = new javax.swing.JMenuItem();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("Automated Pollinator Monitoring");

        visualisationPane2.setBorder(javax.swing.BorderFactory.createTitledBorder("Visualisation Pane"));

        javax.swing.GroupLayout visualisationPane2Layout = new javax.swing.GroupLayout(visualisationPane2);
        visualisationPane2.setLayout(visualisationPane2Layout);
        visualisationPane2Layout.setHorizontalGroup(
            visualisationPane2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 459, Short.MAX_VALUE)
        );
        visualisationPane2Layout.setVerticalGroup(
            visualisationPane2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 0, Short.MAX_VALUE)
        );

        optionsPane1.setBorder(javax.swing.BorderFactory.createTitledBorder("Options Pane"));

        Yolov5_button.setText("Yolov5");

        Yolov8_button.setText("Yolov8");

        ModelChoice.setText("Model: ");

        TrackingVideo.setText("Tracking Video");

        Start.setText("Start Model");

        javax.swing.GroupLayout optionsPane1Layout = new javax.swing.GroupLayout(optionsPane1);
        optionsPane1.setLayout(optionsPane1Layout);
        optionsPane1Layout.setHorizontalGroup(
            optionsPane1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(optionsPane1Layout.createSequentialGroup()
                .addGap(53, 53, 53)
                .addGroup(optionsPane1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(TrackingVideo, javax.swing.GroupLayout.PREFERRED_SIZE, 130, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addGroup(optionsPane1Layout.createSequentialGroup()
                        .addComponent(ModelChoice)
                        .addGap(59, 59, 59)
                        .addComponent(Yolov5_button, javax.swing.GroupLayout.PREFERRED_SIZE, 79, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(18, 18, 18)
                        .addComponent(Yolov8_button)))
                .addContainerGap(73, Short.MAX_VALUE))
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, optionsPane1Layout.createSequentialGroup()
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addComponent(Start)
                .addGap(46, 46, 46))
        );
        optionsPane1Layout.setVerticalGroup(
            optionsPane1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(optionsPane1Layout.createSequentialGroup()
                .addGap(38, 38, 38)
                .addGroup(optionsPane1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(Yolov5_button)
                    .addComponent(Yolov8_button)
                    .addComponent(ModelChoice))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(TrackingVideo)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 32, Short.MAX_VALUE)
                .addComponent(Start)
                .addGap(44, 44, 44))
        );

        statisticsPane1.setBorder(javax.swing.BorderFactory.createTitledBorder("Statistics Pane"));

        SpeciesName.setText("Species Name: ");

        SpeciesInfo.setText("Species Info: ");

        javax.swing.GroupLayout statisticsPane1Layout = new javax.swing.GroupLayout(statisticsPane1);
        statisticsPane1.setLayout(statisticsPane1Layout);
        statisticsPane1Layout.setHorizontalGroup(
            statisticsPane1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(statisticsPane1Layout.createSequentialGroup()
                .addGap(25, 25, 25)
                .addGroup(statisticsPane1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(SpeciesInfo)
                    .addComponent(SpeciesName))
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );
        statisticsPane1Layout.setVerticalGroup(
            statisticsPane1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(statisticsPane1Layout.createSequentialGroup()
                .addGap(26, 26, 26)
                .addComponent(SpeciesName)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(SpeciesInfo)
                .addContainerGap(239, Short.MAX_VALUE))
        );

        Open.setText("Open");

        OpenFile.setText("Open File");
        OpenFile.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                OpenFileActionPerformed(evt);
            }
        });
        Open.add(OpenFile);

        MenuBar.add(Open);

        Export.setText("Export");

        ExportHTML.setText("Export HTML Report");
        Export.add(ExportHTML);

        MenuBar.add(Export);

        setJMenuBar(MenuBar);

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(visualisationPane2, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(optionsPane1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                    .addComponent(statisticsPane1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                .addContainerGap())
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addComponent(optionsPane1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(statisticsPane1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                    .addComponent(visualisationPane2, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                .addContainerGap())
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void OpenFileActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_OpenFileActionPerformed
        FileDialog nameBox = new FileDialog(this, "Open File", FileDialog.LOAD);
        //Display the file chooser dialog & wait
        nameBox.setVisible(true);
        
        //Get the file name
        String fileDirectory = nameBox.getDirectory();
        filename = nameBox.getFile();
        filename = fileDirectory.concat(filename);
    }//GEN-LAST:event_OpenFileActionPerformed

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(MainFrame.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(MainFrame.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(MainFrame.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(MainFrame.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new MainFrame().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JMenu Export;
    private javax.swing.JMenuItem ExportHTML;
    private javax.swing.JMenuBar MenuBar;
    private javax.swing.JLabel ModelChoice;
    private javax.swing.JMenu Open;
    private javax.swing.JMenuItem OpenFile;
    private javax.swing.JLabel SpeciesInfo;
    private javax.swing.JLabel SpeciesName;
    private javax.swing.JButton Start;
    private javax.swing.JCheckBox TrackingVideo;
    private javax.swing.JRadioButton Yolov5_button;
    private javax.swing.JRadioButton Yolov8_button;
    private GUI.OptionsPane optionsPane1;
    private GUI.StatisticsPane statisticsPane1;
    private GUI.VisualisationPane visualisationPane2;
    // End of variables declaration//GEN-END:variables
}
